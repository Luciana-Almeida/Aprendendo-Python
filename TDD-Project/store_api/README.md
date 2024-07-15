# Store API com FastAPI Utilizando TDD

Este projeto foi desenvolvido durante o bootcamp "Coding The Future Vivo - Python AI Backend Developer". Ele é uma implementação de uma API utilizando o framework FastAPI e seguindo a metodologia TDD (Desenvolvimento Orientado a Testes).

## O que é TDD?

TDD é uma sigla para Test Driven Development, ou Desenvolvimento Orientado a Testes. A ideia do TDD é que você trabalhe em ciclos, onde você escreve um teste antes de escrever o código de produção.

### Vantagens do TDD

- Entregar software de qualidade
- Testar procurando possíveis falhas
- Criar testes de integração, testes isolados (unitários)
- Evitar escrever códigos complexos ou que não sigam os pré-requisitos necessários

## Store API

### Objetivo

Essa aplicação tem como objetivo principal trazer conhecimentos sobre o TDD, na prática, desenvolvendo uma API com o Framework Python, FastAPI. Utilizando o banco de dados MongoDB, para validações o Pydantic, para os testes Pytest e entre outras bibliotecas.

### O que é?

- Uma aplicação com fins educativos
- Permite o aprendizado prático sobre TDD com FastAPI + Pytest

### O que não é?

- Uma aplicação que se comunica com apps externas

## Solução Proposta

Desenvolvimento de uma aplicação simples a partir do TDD, que permite entender como criar testes com o pytest. Construindo testes de Schemas, Usecases e Controllers (teste de integração).

## Arquitetura

### Banco de Dados

- MongoDB

### Diagramas de Sequência para o Módulo de Produtos

- Criação de produto
- Listagem de produtos
- Detalhamento de um produto
- Atualização de produto
- Exclusão de produto

## Desafio Final

### Create

- Mapear uma exceção, caso dê algum erro de inserção e capturar na controller

### Update

- Modificar o método de patch para retornar uma exceção de Not Found, quando o dado não for encontrado
- A exceção deve ser tratada na controller, para ser retornada uma mensagem amigável para o usuário
- Ao alterar um dado, a data de updated_at deve corresponder ao time atual, não permitindo modificar updated_at manualmente

### Filtros

- Cadastrar produtos com preços diferentes
- Aplicar um filtro de preço, assim: (price > 5000 and price < 8000)

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **FastAPI**: Framework web para construção da API.
- **Pydantic**: Validações.
- **Pytest**: Biblioteca de testes.
- **Motor**: Driver async para MongoDB.
- **MongoDB**: Banco de dados utilizado.
- **Uvicorn**: Servidor ASGI para FastAPI.
- **Poetry**: Gerenciador de dependências e pacotes para Python.

## Instalação e Execução

### Pré-requisitos

- Docker e Docker Compose instalados.
- Python 3.9 ou superior instalado.
