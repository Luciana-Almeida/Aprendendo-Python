# Sistema Bancário em Python

Este projeto é uma implementação simples de um sistema bancário em Python, desenvolvido durante o bootcamp "Coding The Future Vivo - Python AI Backend Developer". Este é meu primeiro projeto no bootcamp, onde aprendi conceitos fundamentais de programação em Python.

## Funcionalidades

O sistema bancário permite aos usuários realizar três operações básicas: depósito, saque e extrato. Aqui estão as funcionalidades detalhadas:

- **Depósito**: 
  - Permite depósitos de valores positivos.
  - Todos os depósitos são armazenados e exibidos na operação de extrato.
  - Valida se o valor depositado é positivo.

- **Saque**:
  - Permite até 3 saques diários, com um limite de R$ 500,00 por saque.
  - Verifica se o usuário possui saldo suficiente para o saque.
  - Exibe mensagens apropriadas caso o limite de saques ou o valor máximo por saque seja excedido.
  - Todos os saques são armazenados e exibidos na operação de extrato.

- **Extrato**:
  - Lista todas as transações realizadas (depósitos e saques).
  - Exibe o saldo atual da conta.

## O que Aprendi

Neste projeto, aprendi a:

- **Manipular entradas e saídas** em Python usando a função `input()` para capturar dados do usuário e a função `print()` para exibir informações.
- **Estruturas de Controle**: Uso de estruturas condicionais (`if`, `elif`, `else`) para controlar o fluxo do programa.
- **Laços de Repetição**: Implementação de um loop `while` para manter o programa em execução até que o usuário decida sair.
- **Manipulação de Strings**: Uso de métodos de strings como `replace()` para formatação de dados.
- **Validação de Dados**: Verificação de condições para garantir que as operações bancárias sejam válidas (ex: valores positivos, saldo suficiente, limites de saque).
- **Acumulação e Concatenamento**: Acumulação de saldo e concatenação de strings para gerar o extrato das transações.

## Requisitos

- Python 3.6 ou superior
