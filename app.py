
import time
from resources.check_in_wallet import check_in_wallet
from resources.convert_btc_to_new_listing import convert_btc_to_token
from resources.get_btc_balance import get_btc_balance
from resources.get_btc_to_usd_price import get_btc_to_usd_price
from resources.get_latest_listing import get_latest_listing

while(True):

    # Obtendo a última listagem
    latest_listing = get_latest_listing()

    # Verificando se a última listagem está na carteira
    in_wallet = check_in_wallet(latest_listing)

    if in_wallet:
        print(f"A última listagem, {latest_listing}, está na sua carteira.")
    else:
        print(f"A última listagem, {latest_listing}, não está na sua carteira.")
        convert_btc_to_token(latest_listing)
    
    time.sleep(30)