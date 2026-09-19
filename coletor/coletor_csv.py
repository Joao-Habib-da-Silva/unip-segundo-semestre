import csv
import json
from datetime import datetime
from pathlib import Path
import paho.mqtt.client as mqtt
BROKER_MQTT = ""
PORTA_MQTT = 1883
TOPICO_MQTT = "sens/room-1/leituras"
PASTA_DADOS = Path(__file__).resolve().parent
ARQUIVO_CSV = PASTA_DADOS / "leituras.csv"
COLUNAS = [
    "data_hora",
    "dispositivo_id",
    "temperatura_dht_c",
    "umidade_relativa_pct",
    "mq135_adc",
    "ldr_adc"
]
def salvar_no_csv(dados):
    arquivo_existe = ARQUIVO_CSV.exists()
    linha = {
        "data_hora": datetime.now().isoformat(timespec="seconds"),
        "dispositivo_id": dados.get("dispositivo_id", ""),
        "temperatura_dht_c": dados.get("temperatura_dht_c", ""),
        "umidade_relativa_pct": dados.get("umidade_relativa_pct", ""),
        "mq135_adc": dados.get("mq135_adc", ""),
        "ldr_adc": dados.get("ldr_adc", "")
    }
    with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=COLUNAS
        )
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerow(linha)
    print("Leitura salva:", linha)
def quando_conectar(cliente, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Conectado ao broker")
        cliente.subscribe(TOPICO_MQTT)
        print(TOPICO_MQTT)
    else:
        print(reason_code)
def quando_receber_mensagem(cliente, userdata, mensagem):
    try:
        texto_json = mensagem.payload.decode("utf-8")
        dados = json.loads(texto_json)
        print(dados)
        salvar_no_csv(dados)
    except Exception as erro:
        print(erro)
def main():
    if not BROKER_MQTT:
        print("Preencha BROKER_MQTT antes de iniciar o coletor.")
        return
    cliente = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="coletor-csv"
    )
    cliente.on_connect = quando_conectar
    cliente.on_message = quando_receber_mensagem
    print(f"Conectando em {BROKER_MQTT}:{PORTA_MQTT}...")
    cliente.connect(
        BROKER_MQTT,
        PORTA_MQTT,
        keepalive=60
    )
    print("Coletor ativo")
    print("CONTROL C para encerrar")
    cliente.loop_forever()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nColetor encerrado.")