# Cadastro de Pessoas e Carros - API FastAPI

## Visão Geral
Esta aplicação é uma API desenvolvida em Python utilizando FastAPI, conectada a um banco de dados PostgreSQL. Ela permite o cadastro, consulta, atualização e remoção de pessoas e carros.

## Como iniciar a aplicação

1. **Pré-requisitos:**
   - Python 3.10+
   - PostgreSQL
   - Instalar dependências com:
     ```bash
     pip install -r requirements.txt
     ```
2. **Configurar o banco de dados:**
   - Certifique-se de que o PostgreSQL está rodando e crie as tabelas `pessoas` e `carros` conforme necessário.
3. **Executar a API:**
   - Inicie o servidor com:
     ```bash
     uvicorn main:app --reload
     ```
   - A API estará disponível em: http://localhost:8000

## Entidades

### Pessoa
- **Campos:**
  - `id`: inteiro (gerado pelo banco)
  - `nome`: string
  - `idade`: inteiro
  - `email`: string
  - `criado_em`: data de criação (gerado pelo banco)

### Carro
- **Campos:**
  - `id`: inteiro (gerado pelo banco)
  - `nome`: string
  - `ano`: inteiro
  - `marca`: string
  - `preco`: float

## Endpoints das Entidades

### Pessoa
- `GET /pessoas` - Lista todas as pessoas
- `GET /pessoas/{id}` - Busca uma pessoa pelo ID
- `POST /pessoas` - Cria uma nova pessoa
- `PUT /pessoas/{id}` - Atualiza uma pessoa existente
- `DELETE /pessoas/{id}` - Remove uma pessoa

### Carro
- `GET /carros` - Lista todos os carros
- `GET /carros/{id}` - Busca um carro pelo ID
- `POST /carros` - Cria um novo carro
- `PUT /carros/{id}` - Atualiza um carro existente
- `DELETE /carros/{id}` - Remove um carro

## Exemplos de chamadas API

### Pessoa
- **Criar:**
  ```bash
  curl -X POST "http://localhost:8000/pessoas" -H "Content-Type: application/json" -d '{"nome": "João", "idade": 30, "email": "joao@email.com"}'
  ```
- **Listar:**
  ```bash
  curl http://localhost:8000/pessoas
  ```
- **Buscar por ID:**
  ```bash
  curl http://localhost:8000/pessoas/1
  ```
- **Atualizar:**
  ```bash
  curl -X PUT "http://localhost:8000/pessoas/1" -H "Content-Type: application/json" -d '{"nome": "João Silva", "idade": 31, "email": "joao@email.com"}'
  ```
- **Deletar:**
  ```bash
  curl -X DELETE http://localhost:8000/pessoas/1
  ```

### Carro
- **Criar:**
  ```bash
  curl -X POST "http://localhost:8000/carro" -H "Content-Type: application/json" -d '{"nome": "Fusca", "ano": 1980, "marca": "Volkswagen", "preco": 15000.0}'
  ```
- **Listar:**
  ```bash
  curl http://localhost:8000/carros
  ```
- **Buscar por ID:**
  ```bash
  curl http://localhost:8000/carros/1
  ```
- **Atualizar:**
  ```bash
  curl -X PUT "http://localhost:8000/carros/1" -H "Content-Type: application/json" -d '{"nome": "Fusca", "ano": 1981, "marca": "Volkswagen", "preco": 16000.0}'
  ```
- **Deletar:**
  ```bash
  curl -X DELETE http://localhost:8000/carros/1
  ```

## Observações
- Todos os endpoints retornam e recebem dados em formato JSON.
- Utilize ferramentas como Postman, Insomnia ou o próprio Swagger UI do FastAPI (em http://localhost:8000/docs) para testar a API.
