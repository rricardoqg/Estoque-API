# API de Gestão de Estoque

API REST para controle de estoque de pequenos negócios, 
desenvolvida com FastAPI e SQLAlchemy.

## Tecnologias

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Como rodar localmente

### Pré-requisitos
- Python 3.12+

### Instalação

# Clone o repositório
git clone https://github.com/seu-usuario/estoque-api.git
cd estoque-api

# Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install fastapi uvicorn sqlalchemy

# Rode a aplicação
uvicorn app.main:app --reload

A documentação estará disponível em http://127.0.0.1:8000/docs

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /produtos/ | Lista todos os produtos |
| POST | /produtos/ | Cria um novo produto |
| GET | /produtos/{id} | Busca produto por ID |
| PUT | /produtos/{id} | Atualiza um produto |
| DELETE | /produtos/{id} | Deleta um produto |
| GET | /produtos/criticos | Lista produtos abaixo do estoque mínimo |

## Arquitetura

O projeto segue arquitetura em camadas:

- **Router** — define os endpoints
- **Controller** — recebe e responde requisições
- **Service** — regras de negócio
- **Repository** — acesso ao banco de dados