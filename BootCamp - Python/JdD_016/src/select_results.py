from lib.classes.Hero import Hero
from sqlmodel import Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    
    statement = select(Hero)
    result = session.exec(statement)

    heroes = result.all()
    print("_____")
    for hero in heroes:
        print(f"ID: {hero.id}, Name: {hero.name}, Secret Name: {hero.secret_name}, Age: {hero.age}")
