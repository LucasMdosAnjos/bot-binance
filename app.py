
import time

import pytz
from resources.check_in_wallet import check_in_wallet
from resources.convert_btc_to_new_listing import convert_btc_to_token
from resources.get_btc_balance import get_btc_balance
from resources.get_btc_to_usd_price import get_btc_to_usd_price
from resources.get_latest_listing import get_latest_listing
from datetime import datetime
while(True):

    # Obtendo a última listagem
    latest_listing = get_latest_listing()

    # Verificando se a última listagem está na carteira
    in_wallet = check_in_wallet(latest_listing)
    # Definindo o fuso horário para o horário de Brasília (BRT)
    fuso_horario = pytz.timezone('America/Sao_Paulo')

    # Obtendo a data e hora atual no fuso horário de Brasília
    data_hora_atual_brt = datetime.now(fuso_horario)

    # Formatando a data e hora para o formato dd/mm/yyyy HH:MM
    data_hora_formatada = data_hora_atual_brt.strftime("%d/%m/%Y %H:%M")

    if in_wallet:
        msg = f"A última listagem, {latest_listing}, está na sua carteira {data_hora_formatada}."
        # Abrindo o arquivo em modo de anexação
        with open("arquivo.txt", "a") as arquivo:
            # Escrevendo a frase em uma nova linha
            arquivo.write(msg + "\n")
        print(msg)

    else:
        msg = f"A última listagem, {latest_listing}, não está na sua carteira {data_hora_formatada}."
        # Abrindo o arquivo em modo de anexação
        with open("arquivo.txt", "a") as arquivo:
            # Escrevendo a frase em uma nova linha
            arquivo.write(msg + "\n")
        print(msg)
        convert_btc_to_token(latest_listing)
    
    time.sleep(30)