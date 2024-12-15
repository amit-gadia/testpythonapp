import paho.mqtt.client as mqtt
import time 

broker = "broker.mqtt.cool"  # Public MQTT broker
port = 1883

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected",client, userdata, flags, rc)
    print(f"Connected with result code {rc}")

def on_disconnect(client, userdata, rc):
    client.reconnect()
    print("disconnect",client, userdata, rc)
    

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} -> {msg.payload.decode()}")

def mqtt_client():
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(broker, port, 60)
    client.loop_start()
    
    return client



