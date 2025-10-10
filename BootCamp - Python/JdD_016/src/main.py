from lib.classes.Hero import Hero
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parque")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Shark", age=36)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()