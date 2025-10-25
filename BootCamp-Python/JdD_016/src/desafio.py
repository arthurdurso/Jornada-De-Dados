from lib.classes.Livro import Livro
from sqlmodel import Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database_livros.db")

SQLModel.metadata.create_all(engine)

def adicionar_livro(livro: Livro):
    with Session(engine) as session:
        session.add(livro)
        session.commit()

def buscar_livros_por_autor(autor: str):
    with Session(engine) as session:
        result = session.exec(select(Livro).where(Livro.autor == autor))
        livros = result.all()
    return livros

def atualizar_disponibilidade_livro(id_livro: int, disponivel: bool):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        livro.disponivel = disponivel
        session.add(livro)
        session.commit()

def remover_livro(id_livro: int):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        session.delete(livro)
        session.commit()

def ver_todos_livros():
    with Session(engine) as session:
        statement = select(Livro)
        result = session.exec(statement)
        books = result.all()
    return books

if __name__ == "__main__":

    adicionar_livro(Livro(titulo="Morangos Mofados", autor="Caio Fernando Abreu", ano_publicacao="1982", disponivel=True))
    print(ver_todos_livros(),"\n")

    print("Livros de Caio Fernando Abreu: ", buscar_livros_por_autor("Caio Fernando Abreu"),"\n")

    atualizar_disponibilidade_livro(1, False)
    print(ver_todos_livros(),"\n")

    remover_livro(1)
    print(ver_todos_livros(),"\n")