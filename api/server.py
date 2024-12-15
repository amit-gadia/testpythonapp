import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)  # Subscribe to the topic

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} -> {msg.payload.decode()}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

# Start the loop
client.loop_forever()
