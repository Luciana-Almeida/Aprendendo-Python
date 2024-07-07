# Desafio: Sistema Bancário em Python

## Descrição

Este projeto é um sistema bancário implementado em Python, utilizando conceitos de Programação Orientada a Objetos (POO). Uma atualização do sistema anterior, implementando novos conceitos aprendidos e adicionando mais complexidade ao código. O sistema permite a criação de contas bancárias, realização de depósitos, saques, visualização de extratos, criação de novos usuários, e listagem de contas. Foi desenvolvido como parte de um desafio de aprendizado para consolidar conhecimentos em POO.

## Funcionalidades

- Criação de contas bancárias
- Realização de depósitos
- Realização de saques com verificação de limites
- Visualização de extratos com histórico de transações
- Criação de novos usuários
- Listagem de contas

## Estrutura do Código

O sistema é composto por várias classes que representam os diferentes componentes do sistema bancário:

- `Transacao`: Classe abstrata que define um contrato para transações.
- `Deposito`: Classe que representa uma transação de depósito.
- `Saque`: Classe que representa uma transação de saque.
- `Historico`: Classe que armazena o histórico de transações de uma conta.
- `Conta`: Classe que representa uma conta bancária.
- `ContaCorrente`: Subclasse de `Conta` que redefine o limite de saque.
- `Cliente`: Classe que representa um cliente bancário.
- `PessoaFisica`: Subclasse de `Cliente` que adiciona informações específicas para pessoas físicas.

## Aprendizado

Durante o desenvolvimento deste projeto, aprendi a aplicar vários conceitos importantes de POO:

1. **Classes e Objetos**: Como definir classes e criar objetos em Python.
2. **Herança**: Como uma classe pode herdar atributos e métodos de outra classe, permitindo reutilização de código e extensão de funcionalidades.
3. **Polimorfismo**: Como diferentes classes podem ser tratadas de maneira uniforme através de métodos comuns, mesmo que a implementação desses métodos seja diferente.
4. **Encapsulamento**: Como proteger os dados internos de uma classe, expondo apenas o que é necessário através de métodos e propriedades.
5. **Classes Abstratas**: Como definir interfaces para classes, garantindo que certas funções sejam implementadas em subclasses.
6. **Métodos de Classe e Estáticos**: Como usar métodos que não dependem de instâncias da classe para operar.
7. **Gerenciamento de Usuários e Contas**: Como criar, listar e associar usuários a contas bancárias.

## Contribuição

Se você tiver sugestões de melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Obrigada!
Luciana Almeida
