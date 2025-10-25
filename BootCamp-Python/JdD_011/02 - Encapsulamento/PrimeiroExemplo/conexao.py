from sqlite import BancoDeDadosSQLite
from postgre import BancoDeDadosPost
import os

########## SQLITE #############

nome_arquivo = os.path.join(os.path.dirname(__file__),"exemplo.db")
banco_sql = BancoDeDadosSQLite(nome_arquivo)
banco_sql.conectar()

# Inserindo dados na tabela
insert_query_01 = '''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        idade INTEGER,
        cidade TEXT
    );
'''
banco_sql.executar_query(insert_query_01)

# Inserindo dados na tabela
insert_query_01 = '''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        idade INTEGER,
        cidade TEXT
    );
'''
banco_sql.executar_query(insert_query_01)


banco_sql.desconectar()


########## POSTGRE #############
# Realmente não funciona, pois precisa de um banco criado

host = 'localhost'
porta = '5432'
banco = 'nome_do_banco'
usuario = 'usuario'
senha = 'senha'
    
banco_post = BancoDeDadosPost(host, porta, banco, usuario, senha)
banco_post.conectar()

insert_query = """
INSERT INTO usuarios (nome, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
banco_post.executar_query(insert_query)

banco_post.desconectar()
