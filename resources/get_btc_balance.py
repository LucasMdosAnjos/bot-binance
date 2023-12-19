# Função para obter o saldo de BTC
from resources.init_binance_config import CLIENT


def get_btc_balance():
    btc_balance = CLIENT.get_asset_balance(asset='BTC')
    return float(btc_balance['free'])  # 'free' é o saldo disponível