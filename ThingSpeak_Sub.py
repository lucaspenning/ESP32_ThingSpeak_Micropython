import Wifi
Wifi.connect()
import network
from umqtt.robust import MQTTClient
import time
import os
import sys

def cb(topic, msg):
    print((topic, msg))
    freeHeap = float(str(msg,'utf-8'))
    print("free heap size = {} bytes".format(freeHeap))
  
randomNum = int.from_bytes(os.urandom(3), 'little')
myMqttClient = bytes("client"+str(randomNum), 'utf-8')

THINGSPEAK_URL = b"mqtt.thingspeak.com" 
THINGSPEAK_USER_ID = b'780987'
THINGSPEAK_MQTT_API_KEY = b'E4233MZVKTX3ZZVY'
client = MQTTClient(client_id=myMqttClient, 
                    server=THINGSPEAK_URL, 
                    user=THINGSPEAK_USER_ID, 
                    password=THINGSPEAK_MQTT_API_KEY, 
                    ssl=False)

client.set_callback(cb)
try:            
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

THINGSPEAK_CHANNEL_ID = b'780987'
THINGSPEAK_CHANNEL_WRITE_API_KEY = b'IO4INWIR5PFI3KNR'
subscribeTopic = bytes("channels/{:s}/subscribe/fields/field1/{:s}".format(THINGSPEAK_CHANNEL_ID, THINGSPEAK_CHANNEL_READ_API_KEY), 'utf-8')  
client.subscribe(subscribeTopic)

while True:
    try:
        client.wait_msg()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
