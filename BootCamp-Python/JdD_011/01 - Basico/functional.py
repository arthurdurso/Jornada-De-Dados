import pandas as pd
import os

def carregar_csv_e_filtar(arquivo_csv:str, estado:str):

    # Carregar o CSV em DataFrame
    df = pd.read_csv(arquivo_csv)

    # Tratamento de Celulas Vazias
    df = df.dropna()

    # Filtras as linhas
    df_filtrado = df[df['estado'] == estado]

    return df_filtrado

arquivo_csv:str = os.path.join(os.path.dirname(__file__), 'exemplo.csv') # Usa o diretorio do arquivo py para localizar o csv junto 
estado_filtrado:str = 'RJ' #Estado que quero filtrar
df_filtrado = carregar_csv_e_filtar(arquivo_csv, estado_filtrado)

print(df_filtrado)
