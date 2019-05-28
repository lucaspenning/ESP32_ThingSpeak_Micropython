import Wifi
Wifi.connect()
import time
from machine import ADC,Pin
from umqtt.simple import MQTTClient

adc0=ADC(Pin(35))  

SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", SERVER)

CHANNEL_ID = "780987"
WRITE_API_KEY = "IO4INWIR5PFI3KNR"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

temp = 0
valorPublicado = 0

while True:
    temp = adc0.read()/50 
    payload = "field1="+str(temp)
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    time.sleep(20)


