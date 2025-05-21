# Importa o BaseModel do Pydantic para facilitar a validação dos dados
from pydantic import BaseModel

# Modelo de dados para Carro, utilizado para validação e documentação automática
class Carro(BaseModel):
    id: int | None = None  # ID do carro (opcional, geralmente preenchido pelo banco)
    nome: str              # Nome do carro
    ano: int               # Ano de fabricação do carro
    marca: str             # Marca do carro
    preco: float           # Preço do carro