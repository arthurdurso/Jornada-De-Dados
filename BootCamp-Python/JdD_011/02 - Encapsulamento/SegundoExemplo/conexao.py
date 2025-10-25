from dotenv import load_dotenv
from encaps import BancoDeDados

load_dotenv()

########## ENCAPSULADO #############
banco = BancoDeDados('sqlite')
banco.conectar()

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
banco.executar_query(insert_query_01)

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
banco.executar_query(insert_query_01)


banco.desconectar()