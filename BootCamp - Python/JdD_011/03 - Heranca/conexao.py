from etl import ETLCSV

import os

arquivo_csv:str = os.path.join(os.path.dirname(__file__), 'exemplo.csv') # Usa o diretorio do arquivo py para localizar o csv junto 

dados_csv = ETLCSV(arquivo_csv)
dados_csv_transformados = dados_csv.executar_etl()

