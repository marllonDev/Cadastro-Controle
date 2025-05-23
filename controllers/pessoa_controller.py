# Importações necessárias para tipagem, modelo de dados e conexão assíncrona com o banco
from typing import List, Optional
from models.pessoa import Pessoa
import asyncpg

# Controller responsável pela lógica de negócio relacionada à entidade Pessoa
class PessoaController:
    def __init__(self, pool):
        self.pool = pool  # Pool de conexões com o banco de dados

    # Lista todas as pessoas cadastradas no banco
    async def listar_pessoas(self) -> List[Pessoa]:
        async with self.pool.acquire() as conn:
            rows = await conn.fetch('SELECT id, nome, idade, email, criado_em FROM pessoas')
            pessoas = []
            for row in rows:
                criado_em = row['criado_em'].date() if row['criado_em'] else None  # Converte para date
                pessoas.append(Pessoa(id=row['id'], nome=row['nome'], idade=row['idade'], email=row['email'], criado_em=criado_em))
            return pessoas

    # Busca uma pessoa específica pelo ID
    async def obter_pessoa(self, pessoa_id: int) -> Optional[Pessoa]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow('SELECT id, nome, idade, email, criado_em FROM pessoas WHERE id = $1', pessoa_id)
            if row:
                criado_em = row['criado_em'].date() if row['criado_em'] else None
                return Pessoa(id=row['id'], nome=row['nome'], idade=row['idade'], email=row['email'], criado_em=criado_em)
            return None

    # Cria uma nova pessoa no banco de dados
    async def criar_pessoa(self, pessoa: Pessoa) -> Pessoa:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                'INSERT INTO pessoas (nome, idade, email) VALUES ($1, $2, $3) RETURNING id, criado_em',
                pessoa.nome, pessoa.idade, pessoa.email
            )
            pessoa.id = row['id']  # Atribui o ID gerado pelo banco
            pessoa.criado_em = row['criado_em'].date() if row['criado_em'] else None
            return pessoa

    # Atualiza os dados de uma pessoa existente
    async def atualizar_pessoa(self, pessoa_id: int, pessoa: Pessoa) -> Optional[Pessoa]:
        async with self.pool.acquire() as conn:
            result = await conn.execute(
                'UPDATE pessoas SET nome = $1, idade = $2, email = $3 WHERE id = $4',
                pessoa.nome, pessoa.idade, pessoa.email, pessoa_id
            )
            if result.startswith('UPDATE 1'):
                pessoa.id = pessoa_id
                pessoa.criado_em = (await conn.fetchrow('SELECT criado_em FROM pessoas WHERE id = $1', pessoa_id))['criado_em'].date()
                return pessoa
            return None

    # Remove uma pessoa do banco de dados pelo ID
    async def deletar_pessoa(self, pessoa_id: int) -> bool:
        async with self.pool.acquire() as conn:
            result = await conn.execute(f'DELETE FROM pessoas WHERE id = {pessoa_id}')
            return result.startswith('DELETE 1')