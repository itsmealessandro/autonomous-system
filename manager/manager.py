import paho.mqtt.client as mqtt
import json

# Connessione al broker MQTT
client = mqtt.Client()
client.connect("mosquitto", 1883, 60)

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode())
    topic = message.topic
    print(f"Dato ricevuto: {topic} -> {data}")

    # Analisi e decisione
    if "temperature" in topic and data > 24:
        room = topic.split("/")[1]
        client.publish(f"home/{room}/thermostat/command", "cool")

client.subscribe("home/+/+")
client.on_message = on_message
client.loop_forever()
