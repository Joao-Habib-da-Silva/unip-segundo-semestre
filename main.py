from machine import ADC,Pin, I2C
import time
import ujson
import network
import dht
from umqtt.simple import MQTTClient
from bmp280 import BMP280
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
nome_rede = input()
wifi_senha = input()
wifi.connect(nome_rede, wifi_senha)
while not wifi.isconnected():
    time.sleep(1)
#Temos que inserir o endereço IP
brokker_mqtt = ""
topico_mqtt = b"sens/room-1"
cliente = MQTTClient(
    B"esp32-room-01",
    brokker_mqtt
    )
#Necessário colocar o PIN
dht_sensor = dht.DHT22(Pin())
dht_sensor.measure()
temp = dht_sensor.temperature()
umi = dht_sensor.humidity()
#Necessário colocar o PIN
mqt135 = ADC(Pin())
mqt135.atten(ADC.ATTN_11DB)
wind_value = mqt135.read_u16()
#Necessário colocar o PIN
ldr = ADC(Pin())
ldr.atten(ADC.ATTN_11DB)
lum_brut = ldr.read_u16()
data = {
    "temperatura_dht_c": temp,
    "umidade_relativa_pct": umi,
    "mq135_adc": wind_value,
    "ldr_adc": lum_brut
}
try:
    cliente.connect()
    message_json = ujson.dumps(data)
    cliente.publish(
            topico_mqtt,
            message_json
        )
    cliente.disconnect()
except Exception as error:
    print(error)