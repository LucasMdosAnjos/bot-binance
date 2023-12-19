from resources.init_binance_config import CLIENT


def get_latest_listing():
    # Obter as informações mais recentes das listagens
    info = CLIENT.get_exchange_info()
    symbols = [i['symbol'] for i in list(info['symbols']) if 'BTC' in i['symbol']]
    latest_listing = symbols[-1]
    return latest_listing