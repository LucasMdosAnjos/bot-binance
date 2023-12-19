from resources.init_binance_config import CLIENT


def get_token_to_usd_price(symbol:str):
    symbol = symbol.replace('BTC','USDT')
    """Obter a taxa de câmbio atual do TOKEN para USD."""
    ticker = CLIENT.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])