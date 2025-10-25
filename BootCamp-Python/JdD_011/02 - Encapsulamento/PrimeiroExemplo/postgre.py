import psycopg2

class BancoDeDadosPost:
    def __init__(self, host, porta, banco, usuario, senha):
        self.host = host
        self.porta = porta
        self.banco = banco
        self.usuario = usuario
        self.senha = senha
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                port=self.porta,
                database=self.banco,
                user=self.usuario,
                password=self.senha
            ) 
            print("Conexão estabelecida com sucesso!")
        except psycopg2.Error as e:
            print("Erro ao conectar ao banco de dados:", e)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão fechada.")
    
    def executar_query(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print("Query executada com sucesso")
        except psycopg2.Error as e:
            print("Erro ao executar a query:", e)


    def executar_querys(self, query):
        try:
            cursor = self.conexao.cursor()
            cursor.executemany(query)
            self.conexao.commit()
            print("Querys executadas com sucesso")
        except psycopg2.Error as e:
            print("Erro ao executar as querys:", e)
