from pydantic import BaseModel

class Carro(BaseModel):
    id: int | None = None
    nome: str
    ano: int
    marca: str
    preco: float