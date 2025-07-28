from fastapi import FastAPI
from app.views import pokemon_router

app = FastAPI()  # Cria a aplicação FastAPI
app.include_router(pokemon_router, prefix="/pokemon")  # Registra as rotas da Pokédex
