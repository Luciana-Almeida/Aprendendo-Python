# API de Gerenciamento de Atletas

Este projeto é uma implementação simples de uma API de gerenciamento de atletas utilizando FastAPI, desenvolvido durante o bootcamp "Coding The Future Vivo - Python AI Backend Developer".

## Descrição

Este projeto consiste na construção de uma API utilizando FastAPI para gerenciar informações de atletas. A API permite a criação, leitura, atualização e exclusão de dados de atletas. Além disso, a API suporta paginação, filtro por nome e CPF, e manipulação de exceções de integridade de dados.

## Funcionalidades

- **Adicionar Atletas:** Permite adicionar novos atletas ao sistema.
- **Listar Atletas:** Permite listar atletas com suporte a paginação e filtros por nome e CPF.
- **Atualizar Atletas:** Permite atualizar as informações de atletas existentes.
- **Excluir Atletas:** Permite excluir atletas do sistema.
- **Paginação:** Suporte a paginação utilizando a biblioteca `fastapi-pagination`.
- **Manipulação de Exceções:** Manipulação de exceções de integridade de dados utilizando `sqlalchemy.exc.IntegrityError`.

## Estrutura do Projeto

```plaintext
workoutapi/
├── alembic/
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── atletas.py
│   └── schemas.py
├── Dockerfile
├── alembic.ini
├── docker-compose.yml
├── requirements.txt
└── README.md

