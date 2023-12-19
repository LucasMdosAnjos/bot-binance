
from resources.get_btc_to_usd_price import get_btc_to_usd_price
from resources.init_binance_config import CLIENT
import math

def get_symbol_info(symbol):
    """Obter informações sobre um par de negociação específico."""
    return CLIENT.get_symbol_info(symbol)


def convert_btc_to_token(token_symbol):

    # Faça a ordem de conversão (altere para a lógica de mercado ou limite conforme necessário)
    ticker = CLIENT.get_symbol_ticker(symbol=token_symbol)
    valor_token_em_btc = float(ticker['price']) #valor do token em bitcoin exemplo 1ACE é equivalente a 0.00033508 bitcoins que é equivalente a 14 dolares agora
    btc_value_in_usd = get_btc_to_usd_price()
    ten_dollars_in_btc = 10 / btc_value_in_usd #quantos são 10 dolares em bitcoin que no caso de agora sao 0,00024

    quantidade_a_comprar_do_token = ten_dollars_in_btc/valor_token_em_btc
    order = CLIENT.order_market_buy(
        symbol=token_symbol,
        quantity=round(quantidade_a_comprar_do_token,1)
    )

    print("Ordem realizada:", order)