# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa você vai construir uma API REST simples usando o framework FastAPI. A ideia é aprender a definir rotas, usar modelos Pydantic para validação, lidar com erros HTTP e aproveitar a documentação automática gerada pelo FastAPI.

## 📝 Tasks

### 🛠️ 1) Criar endpoints básicos

#### Descrição
Implemente endpoints para listar, recuperar, criar, atualizar e remover recursos (por exemplo: itens de uma loja) usando uma estrutura em memória.

#### Requirements
Completed program should:

- Suportar `GET /items` para listar todos os itens
- Suportar `GET /items/{id}` para recuperar um item por id
- Suportar `POST /items` para criar um item (validação com Pydantic)
- Suportar `PUT /items/{id}` para atualizar um item
- Suportar `DELETE /items/{id}` para remover um item

### 🛠️ 2) Validação e tratamento de erros

#### Descrição
Use `pydantic` para validar os dados de entrada e lance `HTTPException` quando apropriado (por exemplo, item não encontrado ou ID duplicado).

#### Requirements

- Modelo `Item` com campos `id`, `name`, `description` (opcional) e `price`
- Respostas corretas com códigos HTTP apropriados (201 para criação, 204 para exclusão sem conteúdo, 404 quando não encontrado)

### 🛠️ 3) Documentação e execução

#### Descrição
Verifique a documentação automática do FastAPI (OpenAPI/Swagger) e inclua instruções de execução local.

#### Requirements

- Instruções para instalar dependências e executar a API localmente
- Demonstração de rotas e exemplos de payloads

## 🧾 Anexos / Arquivos fornecidos

- `starter-code.py`: Exemplo de API que serve como ponto de partida
- `requirements.txt`: Dependências necessárias

## Como executar (local)

1. Crie um ambiente virtual (recomendado): `python3 -m venv .venv` e ative:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\\Scripts\\Activate.ps1`
2. Instale dependências:
   - `pip install -r requirements.txt`
3. Execute a API:
   - `python starter-code.py`
4. Abra a documentação interativa em: `http://127.0.0.1:8000/docs`

## Critérios de avaliação

- Endpoints implementados e funcionando conforme especificado
- Uso apropriado de modelos Pydantic para validação
- Tratamento de erros HTTP com mensagens úteis
- Documentação acessível via `/docs`

Boa sorte! Explore a documentação do FastAPI e divirta-se construindo APIs.
