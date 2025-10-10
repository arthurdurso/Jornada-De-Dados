import os
import sqlite3
import psycopg2


class BancoDeDados:
    def __init__(self, tipo_banco):
        self.tipo_banco = tipo_banco
        self.conexao = None

    def conectar(self):
        if self.tipo_banco == 'sqlite':
            try:
                nome_arquivo = os.path.join(os.path.dirname(__file__), os.getenv('NOME_ARQUIVO_SQLITE'))
                self.conexao = sqlite3.connect(nome_arquivo)
                print("Conexão SQLite estabelecida com sucesso!")
            except sqlite3.Error as e:
                print("Erro ao conectar ao banco de dados SQLite:", e)
        elif self.tipo_banco == 'postgres':
            try:
                host = os.getenv('HOST_PG')
                porta = os.getenv('PORTA_PG')
                banco = os.getenv('BANCO_PG')
                usuario = os.getenv('USUARIO_PG')
                senha = os.getenv('SENHA_PG')
                self.conexao = psycopg2.connect(
                    host=host,
                    port=porta,
                    database=banco,
                    user=usuario,
                    password=senha
                ) 
                print("Conexão PostgreSQL estabelecida com sucesso!")
            except psycopg2.Error as e:
                print("Erro ao conectar ao banco de dados PostgreSQL:", e)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            if self.tipo_banco == 'sqlite':
                print("Conexão SQLite fechada.")
            elif self.tipo_banco == 'postgres':
                print("Conexão PostgreSQL fechada.")
    
    def executar_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executada com sucesso")
        except (sqlite3.Error, psycopg2.Error) as e:
            print("Erro ao executar a query:", e)