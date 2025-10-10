import os
import pandas as pd
import sqlite3

# Classe 'base'
class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados deve ser implementado nas classes filhas.")
    
    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar_dados deve ser implementado nas classes filhas.")
    
    def carregar_dados(self, dados_transformados):
        raise NotImplementedError("Método carregar_dados deve ser implementado nas classes filhas.")
    
    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        return self.carregar_dados(dados_transformados)
    
# Classe para CSV
class ETLCSV(ETLProcess):
    def extrair_dados(self):
        return pd.read_csv(self.fonte_dados)
    
    def transformar_dados(self, dados):
        #Converter todas as letras em maiusculas
        return dados.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    
    def carregar_dados(self, dados_transformados):
        print("Dados transformados:", dados_transformados)
        nome_arquivo = os.path.join(os.path.dirname(__file__), os.getenv('NOME_ARQUIVO_SQLITE'))
        with sqlite3.connect(nome_arquivo) as conexao:
            dados_transformados.to_sql("exemplo.db", conexao, if_exists='replace', index=False)
