from binance.client import Client
import os
from time import time

def init_binance_config()-> Client:

    # Configuração das chaves da API
    key = os.getenv('BINANCE_API_KEY')
    secret = os.getenv('BINANCE_API_SECRET')
    client = Client(key, secret)

    # Sincronizar com o tempo do servidor
    client.ping()
    time_res = client.get_server_time()
    client_time = int(time_res['serverTime'])

    # Ajustar a diferença de tempo
    client.timestamp_offset = client_time - int(time() * 1000)

    return client

CLIENT = init_binance_config()