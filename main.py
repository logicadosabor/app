import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .database import engine, Base
from .api import api_router
import uvicorn

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Sistema de Monitoramento de Boas Práticas na Higienização de Vegetais",
    description="API para o Restaurante Lógica do Sabor",
    version="1.0.0"
)

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar a origem exata
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar diretório estático para arquivos de evidência
os.makedirs("static/evidencias", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir todas as rotas da API
app.include_router(api_router)

# Ponto de entrada para execução direta
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
