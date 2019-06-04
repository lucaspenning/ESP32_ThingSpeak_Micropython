import Wifi
Wifi.connect()
import time
from machine import ADC,Pin
from umqtt.simple import MQTTClient
import dht 

adc0=ADC(Pin(35))  
sensor = dht.DHT11(Pin(14))

SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", SERVER)

CHANNEL_ID = "ID_DO_CANAL"
WRITE_API_KEY = "WRITE_API_KEY"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

while True:
    sensor.measure()
    temperatura = sensor.temperature()
    print(temperatura)
    umidade = sensor.humidity()
    print(umidade)
    luminosidade = adc0.read()/40.95 
    print(luminosidade)
    payload = "field1="+str(luminosidade) + "&field2="+str(temperatura) + "&field3="+str(umidade)
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    time.sleep(20)
