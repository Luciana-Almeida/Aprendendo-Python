# Desafio 30: Crie um programa que leia um número inteiro e mostra na tala se ele é PAR ou IMPAR.

numero = int(input("Informe um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é ÍMPAR")
