from datetime import date
from pydantic import BaseModel

class Pessoa(BaseModel):
    id: int | None = None
    nome: str
    idade: int
    email: str
    criado_em: date | None = None