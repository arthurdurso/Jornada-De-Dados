import pandas as pd

class CsvProcessor:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtar_por(self, colunas:list, atributos:list):
        if len(colunas) != len(atributos):
            raise ValueError("Colunas e atributos não tem a mesma quantidade.")
        
        if len(colunas) == 0:
            return self.df
        
        df_filtrado = self.df  # Inicia com o DataFrame completo
        
        for coluna, atributo in zip(colunas, atributos):
            df_filtrado = df_filtrado[df_filtrado[coluna] == atributo]
        
        return df_filtrado