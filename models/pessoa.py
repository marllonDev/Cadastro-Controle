# Importa o tipo date para o campo de data de criação
from datetime import date
# Importa o BaseModel do Pydantic para facilitar a validação dos dados
from pydantic import BaseModel

# Modelo de dados para Pessoa, utilizado para validação e documentação automática
class Pessoa(BaseModel):
    id: int | None = None  # ID da pessoa (opcional, geralmente preenchido pelo banco)
    nome: str              # Nome da pessoa
    idade: int             # Idade da pessoa
    email: str             # Email da pessoa
    criado_em: date | None = None  # Data de criação do registro (opcional)