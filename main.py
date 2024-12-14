from flask import *

from mqtt_connector import mqtt_client

app = Flask("__main__")


mqtt_client_var = mqtt_client()

@app.route("/")
def root_app():
    
    number = request.args.get("phno")    
    print(mqtt_client_var.is_connected(),"mqtt_client_varmqtt_client_var")
    
    mqtt_client_var.publish("test/topic", number)
    return "hello"




@app.route("/publishOnTopic")
def publishOnTopic():
    topicname = request.args.get("topicname")
    msg = request.args.get("msg")
    mqtt_client_var.publish(topicname, msg)
    return "publishOnTopic"

@app.route("/addNewTopic")
def addNewMQTTTopic():
    topicname = request.args.get("topicname")
    mqtt_client_var.subscribe(topicname)
    
    return "addNewTopic"


app.run(debug=True,host='0.0.0.0',port=443)