from fastapi import APIRouter, HTTPException, status, Request
from models.carro import Carro
from controllers.carro_controller import CarroController
from typing import List

router = APIRouter()

# Helper para obter o controller a partir do app.state.pool
async def get_controller(request: Request) -> CarroController:
    return CarroController(request.app.state.pool)

@router.get("/carros", response_model=List[Carro])
async def listar_carros(request: Request):
    controller = await get_controller(request)
    return await controller.listar_carros()

@router.get("/carros/{carros_id}", response_model=Carro)
async def obter_carro(carros_id: int, request: Request):
    controller = await get_controller(request)
    carro = await controller.obter_carro(carros_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return carro