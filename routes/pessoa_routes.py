# Importa as dependências necessárias do FastAPI e módulos do projeto
from fastapi import APIRouter, HTTPException, Request, status
from models.pessoa import Pessoa
from controllers.pessoa_controller import PessoaController
from typing import List

router = APIRouter()

# Função auxiliar para obter o controller de Pessoa a partir do pool de conexões
async def get_controller(request: Request) -> PessoaController:
    return PessoaController(request.app.state.pool)

# Endpoint para listar todas as pessoas cadastradas
@router.get("/pessoas", response_model=List[Pessoa])
async def listar_pessoas(request: Request):
    controller = await get_controller(request)
    return await controller.listar_pessoas()

# Endpoint para obter uma pessoa específica pelo ID
@router.get("/pessoas/{pessoa_id}", response_model=Pessoa)
async def obter_pessoa(pessoa_id: int, request: Request):
    controller = await get_controller(request)
    pessoa = await controller.obter_pessoa(pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa

# Endpoint para criar uma nova pessoa
@router.post("/pessoas", response_model=Pessoa, status_code=status.HTTP_201_CREATED)
async def criar_pessoa(pessoa: Pessoa, request: Request):
    controller = await get_controller(request)
    return await controller.criar_pessoa(pessoa)

# Endpoint para atualizar os dados de uma pessoa existente
@router.put("/pessoas/{pessoa_id}", response_model=Pessoa)
async def atualizar_pessoa(pessoa_id: int, pessoa: Pessoa, request: Request):
    controller = await get_controller(request)
    pessoa_atualizada = await controller.atualizar_pessoa(pessoa_id, pessoa)
    if not pessoa_atualizada:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa_atualizada

# Endpoint para deletar uma pessoa pelo ID
@router.delete("/pessoas/{pessoa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_pessoa(pessoa_id: int, request: Request):
    controller = await get_controller(request)
    sucesso = await controller.deletar_pessoa(pessoa_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return None