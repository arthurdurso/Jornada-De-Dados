from fastapi import FastAPI
from src.lib.classes.models import Base
from src.lib.classes.db import engine
from src.controllers.controller import item_router


app = FastAPI()

# Criar todas as tabelas no banco de dados
Base.metadata.create_all(engine)

# Incluir as rotas do controller
app.include_router(item_router)