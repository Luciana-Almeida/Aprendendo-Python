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

## Tecnologias Utilizadas
- Python: Linguagem de programação utilizada.
- FastAPI: Framework web para construção da API.
- SQLAlchemy: ORM para manipulação do banco de dados.
- Alembic: Ferramenta para migrações do banco de dados.
- Docker: Utilizado para containerização da aplicação.
- PostgreSQL: Banco de dados utilizado.
- Instalação e Execução
- Pré-requisitos
- Docker e Docker Compose instalados.
- Python 3.9 ou superior instalado.
- Passos para Instalação


### 1. Clone o repositório
git clone https://github.com/seu-usuario/api-gerenciamento-atletas.git
cd api-gerenciamento-atletas

### 2. Crie um ambiente virtual
python -m venv .env
source .env/bin/activate  # No Windows use: .env\Scripts\activate

### 3. Instale dependências
pip install -r requirements.txt

### 4. Execute migrações do banco de dados
alembic upgrade head

### 5. Inicie a aplicação
uvicorn app.main:app --host 0.0.0.0 --port 8000

### 6. Acesse a documentação da API
Abra o navegador e acesse http://127.0.0.1:8000/docs para visualizar e interagir com a documentação da API.


## Contribuição
Se você quiser contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório, criar uma branch para suas alterações e enviar um pull request.

- Faça um fork do projeto.
- Crie uma branch para sua feature (git checkout -b feature/nova-feature).
- Commit suas alterações (git commit -am 'Adiciona nova feature').
- Faça o push para a branch (git push origin feature/nova-feature).
- Crie um novo Pull Request.

Contato: Luciana Almeida - www.linkedin.com/in/luciana-almeida-ferreira



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

