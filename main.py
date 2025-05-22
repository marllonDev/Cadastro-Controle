# Importa as bibliotecas necessárias do FastAPI e asyncpg para a aplicação
from fastapi import FastAPI
import asyncpg
import asyncio
from routes.pessoa_routes import router as pessoa_router
from routes.carro_routes import router as carro_router
from fastapi.middleware.cors import CORSMiddleware

# Cria uma instância do FastAPI
app = FastAPI()

# Configura o middleware CORS para permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a URL de conexão com o banco de dados PostgreSQL
DATABASE_URL = "postgresql://adm:adm@localhost:5432/postgres"

# Função assíncrona para conectar ao banco de dados
async def connect_db():
    return await asyncpg.create_pool(DATABASE_URL)

# Evento de inicialização do aplicativo para criar o pool de conexões
@app.on_event("startup")
async def startup():
    app.state.pool = await connect_db()

# Evento de encerramento do aplicativo para fechar o pool de conexões
@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()

# Inclui os routers para as rotas de pessoa e carro
app.include_router(pessoa_router)
app.include_router(carro_router)

# Rota raiz que retorna uma mensagem de sucesso na conexão com o Postgres
@app.get("/")
async def root():
    return {"message": "API FastAPI conectada ao Postgres!"}