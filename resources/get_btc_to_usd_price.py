from resources.init_binance_config import CLIENT


def get_btc_to_usd_price():
    """Obter a taxa de câmbio atual do BTC para USD."""
    ticker = CLIENT.get_symbol_ticker(symbol="BTCUSDT")
    return float(ticker['price'])