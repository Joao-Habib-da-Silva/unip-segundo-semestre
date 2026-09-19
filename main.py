from machine import ADC,Pin,I2C
import time
import ujson
import network
import dht
from umqtt.simple import MQTTClient
from bmp280 import BMP280
wifi=network.WLAN(network.STA_IF)
wifi.active(True)
nome_rede=input()
wifi_senha=input()
wifi.connect(nome_rede,wifi_senha)
while not wifi.isconnected():
    time.sleep(1)
broker_mqtt=""
topico_mqtt=b"sens/room-1"
cliente=MQTTClient(b"esp32-room-01",broker_mqtt)
i2c=I2C(0,scl=Pin(26),sda=Pin(27))
dht_sensor=dht.DHT22(Pin(13))
dht_sensor.measure()
temp=dht_sensor.temperature()
umi=dht_sensor.humidity()
mq135=ADC(Pin(14))
mq135.atten(ADC.ATTN_11DB)
mq135_value=mq135.read_u16()
ldr=ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)
lum_brut=ldr.read_u16()
data={
    "temperatura_dht_c":temp,
    "umidade_relativa_pct":umi,
    "mq135_adc":mq135_value,
    "ldr_adc":lum_brut
}
try:
    cliente.connect()
    message_json=ujson.dumps(data)
    cliente.publish(topico_mqtt,message_json)
    cliente.disconnect()
    print(message_json)
except Exception as error:
    print(error)