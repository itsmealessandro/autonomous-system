import paho.mqtt.client as mqtt
import json
import random
import time
import threading
import logging

# Configura il logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Carica la configurazione dell'ambiente
try:
    with open("/app/env/env.json") as f:
        config = json.load(f)
    logging.info("File env.json caricato correttamente.")
except Exception as e:
    logging.error(f"Errore durante la lettura del file env.json: {e}")
    exit(1)

# Connessione al broker MQTT
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)  # Usa l'API di callback versione 2
try:
    client.connect("mosquitto", 1883, 60)
    logging.info("Connesso al broker MQTT.")
except Exception as e:
    logging.error(f"Errore durante la connessione al broker MQTT: {e}")
    exit(1)

# Funzione per pubblicare i dati dei sensori
def publish_sensor_data(room, sensor):
    while True:
        try:
            # Genera un valore casuale per il sensore
            value = round(random.uniform(sensor["min_value"], sensor["max_value"]), 2)
            # Crea il topic MQTT (es. home/room1/temperature)
            topic = f"home/{room['name']}/{sensor['type']}"
            # Pubblica il valore sul topic
            client.publish(topic, json.dumps({"value": value}))
            logging.info(f"Pubblicato: {topic} -> {value}")
        except Exception as e:
            logging.error(f"Errore durante la pubblicazione dei dati: {e}")
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
        logging.info(f"Avviato thread per {room['name']}/{sensor['type']}")

# Loop per mantenere la connessione attiva
try:
    client.loop_forever()
except KeyboardInterrupt:
    logging.info("Interruzione manuale del programma.")
except Exception as e:
    logging.error(f"Errore durante l'esecuzione del loop MQTT: {e}")