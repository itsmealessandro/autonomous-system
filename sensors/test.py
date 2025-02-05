import paho.mqtt.client as mqtt, time

# Creazione del client MQTT
mqttc = mqtt.Client()

mqttc.connect("mosquitto-container", 1883, 60)

i=0
while(i<10):
    i=i+1
    time.sleep(1)
    # Invia un messaggio al topic "test/topic"
    mqttc.publish("test", "Ciao Mosquitto!")
    print("published hello!")
mqttc.disconnect()
