from fastapi import FastAPI
import asyncpg
import asyncio
from routes.pessoa_routes import router as pessoa_router
from routes.carro_routes import router as carro_router

app = FastAPI()

DATABASE_URL = "postgresql://adm:adm@localhost:5432/postgres"

async def connect_db():
    return await asyncpg.create_pool(DATABASE_URL)

@app.on_event("startup")
async def startup():
    app.state.pool = await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await app.state.pool.close()

app.include_router(pessoa_router)
app.include_router(carro_router)

@app.get("/")
async def root():
    return {"message": "API FastAPI conectada ao Postgres!"}