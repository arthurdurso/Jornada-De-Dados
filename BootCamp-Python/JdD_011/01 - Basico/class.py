import pandas as pd
import os

class ProcessadorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None

    def carregar_csv(self):
        # Carregar o CSV em DataFrame
        self.df = pd.read_csv(self.arquivo_csv)

    def remover_celulas_vazias(self):
        # Tratamento de Celulas Vazias
        self.df = self.df.dropna()

    def filtrar_por_estado(self, estado):
        # Filtras as linhas
        self.df = self.df[self.df['estado'] == estado]

    def processar(self, estado):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)

        return self.df


arquivo_csv:str = os.path.join(os.path.dirname(__file__), 'exemplo.csv') # Usa o diretorio do arquivo py para localizar o csv junto 
estado_filtrado:str = 'RJ' #Estado que quero filtrar


processador = ProcessadorCSV(arquivo_csv)
df_filtrado =  processador.processar(estado_filtrado)

print(df_filtrado)