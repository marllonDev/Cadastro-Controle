# Importações necessárias para o modelo de dados, tipagem e conexão assíncrona com o banco
from models.carro import Carro
from typing import List, Optional
import asyncpg

# Controller responsável pela lógica de negócio relacionada à entidade Carro
class CarroController:
    def __init__(self, pool):
        self.pool = pool  # Pool de conexões com o banco de dados
    
    # Lista todos os carros cadastrados no banco
    async def listar_carros(self) -> List[Carro]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch('SELECT id, nome, ano, marca, preco FROM carros')
            return [Carro(id=row['id'], nome=row['nome'], ano=row['ano'], marca=row['marca'], preco=row['preco']) for row in rows]
    
    # Busca um carro específico pelo ID
    async def obter_carro(self, carro_id: int) -> Optional[Carro]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(f'SELECT id, nome, ano, marca, preco FROM carros WHERE id = {carro_id}')
            if row:
                return Carro(id=row['id'], nome=row['nome'], ano=row['ano'], marca=row['marca'], preco=row['preco'])
            return None

    # Cria um novo carro no banco de dados
    async def criar_carro(self, carro: Carro) -> Carro:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                'INSERT INTO carros (nome, ano, marca, preco) VALUES($1, $2, $3, $4) RETURNING id', carro.nome, carro.ano, carro.marca, carro.preco
                )
            carro_id = row['id']  # Atribui o ID gerado pelo banco
            carro.id = carro_id
            return carro

    # Atualiza os dados de um carro existente
    async def atualizar_carro(self, carro_id: int, carro: Carro) -> Optional[Carro]:
        async with self.pool.acquire() as conn:
            result = await conn.execute(
                'UPDATE carros SET nome = $1, ano = $2, marca = $3, preco = $4 WHERE id = $5', carro.nome, carro.ano, carro.marca, carro.preco, carro_id
            )
            if result.startswith('UPDATE 1'):
                carro.id = carro_id
                return carro
            return None

    # Remove um carro do banco de dados pelo ID
    async def deletar_carro(self, carro_id: int) -> bool:
        async with self.pool.acquire() as conn:
            result = await conn.execute('DELETE FROM carros WHERE id = $1', carro_id)
            return result.startswith('DELETE 1')