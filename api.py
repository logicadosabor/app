from fastapi import APIRouter, Depends
from ..routes import users, vegetais, solucoes, processos, auth

api_router = APIRouter()

# Incluir todas as rotas
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(vegetais.router)
api_router.include_router(solucoes.router)
api_router.include_router(processos.router)
