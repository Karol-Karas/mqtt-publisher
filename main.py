import threading
import paho.mqtt.client as mqtt
import json
from datetime import datetime

mqttclient = mqtt.Client("clientId-DXY6rkIy2p111", clean_session=False)
# mqttclient.username_pw_set("username", "password")
mqttclient.connect("broker.hivemq.com")

message = {
        "sensor": "gps",
        "time": 1621930000,
        "data": {
            "lat": 53.11,
            "lng": 23.14
        }
}

def pub():
    mqttclient.publish("sensor/loragps", payload=json.dumps(message), retain=False)
    threading.Timer(5, pub).start()
    message["data"]["lat"] += 0.0001
    message["data"]["lng"] -= 0.0001
    message["time"] += 10
    print(message)

    conv_time = datetime.fromtimestamp(message["time"])
    print(conv_time)

pub()
