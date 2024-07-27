# Desafio 35: Desenvolva um programa que leia o comprimento de três retas a diga ao usuário se elas podem ou não formar um triângulo.

a = input("Informe o comprimento do primeiro lado: ")
b = input("Informe o comprimento do segundo lado: ")
c = input("Informe o comprimento do terceiro lado: ")

if (a + b > c) and (a + c > b) and (b + c > a):
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
    