from resources.init_binance_config import CLIENT


def check_in_wallet(symbol:str):
    # Verificar se o símbolo está na carteira
    symbol = symbol.replace('BTC','').strip()
    account = CLIENT.get_account()
    balances = {balance['asset']: balance['free'] for balance in account['balances']}
    
    return symbol in balances and float(balances[symbol]) > 0
