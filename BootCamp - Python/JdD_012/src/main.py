from interface.classes.csv_class import CsvProcessor
import os

caminho_csv = os.path.join(os.path.dirname(__file__),'exemplo.csv')

arquivo_csv = CsvProcessor(caminho_csv)
arquivo_csv.carregar_csv()

print(arquivo_csv.filtar_por(['estado','data'], ['SP', '20/01/2024']))