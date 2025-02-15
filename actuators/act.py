import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Comando ricevuto: {message.topic} -> {message.payload.decode()}")

client = mqtt.Client()
client.connect("mosquitto", 1883, 60)
client.subscribe("home/+/+/command")
client.on_message = on_message
client.loop_forever()
