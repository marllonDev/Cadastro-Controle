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


## Sobre mim
𝐒𝐞𝐧𝐢𝐨𝐫 𝐃𝐚𝐭𝐚 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫

Com 𝟰+ 𝘆𝗲𝗮𝗿𝘀 de experiência no mundo da tecnologia, eu me desenvolvo na interseção entre engenharia de dados e inovação. Atualmente, estou criando ecossistemas de dados escaláveis como 𝗦𝗲𝗻𝗶𝗼𝗿 𝗗𝗮𝘁𝗮 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿. Aperfeiçoei minhas habilidades em setores que moldam as economias - desde 𝗺𝗮𝗶𝗼𝗿𝗲𝘀 𝗯𝗮𝗻𝗰𝗼𝘀 𝗱𝗼 𝗕𝗿𝗮𝘀𝗶𝗹 e 𝘀𝗲𝗴𝘂𝗿𝗮𝗱𝗼𝗿𝗮𝘀 𝗹𝗶𝗱𝗲𝗿𝗲𝘀 𝗺𝘂𝗻𝗱𝗶𝗮𝗶𝘀, até o 𝗺𝗮𝗶𝗼𝗿 𝗽𝗿𝗼𝗱𝘂𝘁𝗼𝗿 𝗱𝗲 𝗰𝗲𝗿𝘃𝗲𝗷𝗮 do mundo, e agora estou causando impacto no 𝘀𝗲𝘁𝗼𝗿 𝗱𝗼 𝗰𝗿𝗲𝗱𝗶𝘁𝗼. 

💡 𝗣𝗼𝗿𝗾𝘂𝗲 𝗲𝘂 𝗺𝗲 𝗱𝗲𝘀𝘁𝗮𝗰𝗼? \
Eu 𝗮𝗿𝗾𝘂𝗶𝘁𝗲𝘁𝗼 𝗽𝗶𝗽𝗲𝗹𝗶𝗻𝗲𝘀 de dados robustos para 𝗙𝗼𝗿𝘁𝘂𝗻𝗲 𝟱𝟬𝟬 𝗽𝗹𝗮𝘆𝗲𝗿𝘀, otimizei os sistemas legados para nuvem (𝗔𝗪𝗦/𝗔𝘇𝘂𝗿𝗲) que forneceram insights acionáveis por meio de estruturas ETL/ELT escaláveis. Da análise financeira em tempo real à otimização da cadeia de suprimentos de cervejarias, eu transformo dados brutos em ativos estratégicos. 

✨ 𝗔𝗹𝗲𝗺 𝗱𝗼 𝗰𝗼𝗱𝗶𝗴𝗼: \
Um aprendiz permanente obcecado com a democratização de dados e a solução ágil de problemas. Vamos nos conectar se você estiver 𝗮𝗽𝗮𝗶𝘅𝗼𝗻𝗮𝗱𝗼 sobre a nuvem, eficiência do 𝗗𝗲𝘃𝗢𝗽𝘀 ou o papel dos dados na transformação dos setores!

Me siga: [Linkedin](https://www.linkedin.com/in/marllonzuc/) \
Meu Blog: [Blog](https://datatrends.me/)


![Logo](https://media.licdn.com/dms/image/v2/D4D03AQEFlFTNmApBhQ/profile-displayphoto-shrink_800_800/B4DZbt9iTrHsAc-/0/1747749054334?e=1753315200&v=beta&t=VfBvrDxLmoAYccE0DW63MbSLz_ao9Xp_HQAfcyP7-og)

