
import Wifi
Wifi.connect()
import network
from umqtt.robust import MQTTClient
import time
import os
import sys
import gc

def cb(topic, msg):
    freeHeap = float(str(msg,'utf-8'))
    print(freeHeap)
  
randomNum = int.from_bytes(os.urandom(3), 'little')
myMqttClient = bytes("client"+str(randomNum), 'utf-8')

THINGSPEAK_URL = b"mqtt.thingspeak.com" 
THINGSPEAK_USER_ID = b'ID_DO_CANAL'
THINGSPEAK_MQTT_API_KEY = b'CHAVE_API_MQTT'
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

THINGSPEAK_CHANNEL_ID = b'ID_DO_CANAL'
THINGSPEAK_CHANNEL_WRITE_API_KEY = b'CHAVE_WRITE_DO_CANAL'

PUBLISH_PERIOD_IN_SEC = 30 

while True:
    try:
#Publicar no ThingSpeak      
        freeHeapInBytes = gc.mem_free()
        credentials = bytes("channels/{:s}/publish/{:s}".format(THINGSPEAK_CHANNEL_ID, THINGSPEAK_CHANNEL_WRITE_API_KEY), 'utf-8')  
        payload = bytes("field1={:.1f}\n".format(freeHeapInBytes), 'utf-8')
        client.publish(credentials, payload)
        print("Publicado com sucesso o valorde de:" + str(freeHeapInBytes))
#Ler do ThingSpeak      
        subscribeTopic = bytes("channels/{:s}/subscribe/fields/field1/{:s}".format(THINGSPEAK_CHANNEL_ID, THINGSPEAK_CHANNEL_WRITE_API_KEY), 'utf-8')  
        client.subscribe(subscribeTopic)
        client.wait_msg()
#Intervalo de tempo para repetir o c鐠愮珡igo
        time.sleep(PUBLISH_PERIOD_IN_SEC)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
