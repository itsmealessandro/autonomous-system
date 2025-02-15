import paho.mqtt.client as mqtt
import json
import random
import time
import threading

# Carica la configurazione dell'ambiente
with open("/app/env/env.json") as f:  # Percorso corretto nel container
    config = json.load(f)

# Connessione al broker MQTT
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

# Funzione per pubblicare i dati dei sensori
def publish_sensor_data(room, sensor):
    while True:
        # Genera un valore casuale per il sensore
        value = round(random.uniform(sensor["min_value"], sensor["max_value"]), 2)
        # Crea il topic MQTT (es. home/room1/temperature)
        topic = f"home/{room['name']}/{sensor['type']}"
        # Pubblica il valore sul topic
        client.publish(topic, json.dumps({"value": value}))
        print(f"Pubblicato: {topic} -> {value}")
        # Attendi prima di pubblicare il prossimo valore
        time.sleep(5)

# Avvia un thread per ogni sensore in ogni stanza
threads = []
for room in config["rooms"]:
    for sensor in room["sensors"]:
        thread = threading.Thread(target=publish_sensor_data, args=(room, sensor))
        thread.daemon = True  # Il thread si chiuderà quando il programma principale termina
        thread.start()
        threads.append(thread)

# Loop per mantenere la connessione attiva
client.loop_forever()
