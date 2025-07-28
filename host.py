"""
Handles publish and callbacks for board
"""

from time import sleep
import paho.mqtt.client as mqtt

from handlers import Subscriptions

BROKER_ADDRESS = "broker.emqx.io"
BROKER_PORT = 1883

def on_conect(client, userdata, connect_flags, reason_code, properties):
    print("Connected")

def on_message(client, userdate, msg):
    Subscriptions.subs[msg.topic](msg)
    print("I received something")
    pass

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_conect
mqttc.on_message = on_message

mqttc.connect(BROKER_ADDRESS, BROKER_PORT)

mqttc.subscribe(topic="stm_test")

mqttc.loop_forever()