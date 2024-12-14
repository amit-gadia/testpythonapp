import paho.mqtt.client as mqtt
import time 

broker = "broker.hivemq.com"  # Public MQTT broker
port = 1883                  # Standard MQTT port
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect

client.connect(broker, port, 60)

# Publish a message
client.loop_start()

for i in range(100):
    
    time.sleep(2)
    client.publish(topic, "Hello MQTT!")
