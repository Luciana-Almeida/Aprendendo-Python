# Desafio 25: Crie um programa que leia um nome de uma pessoa e diga se ela tem “Silva” no nome.

nome = input("Informe o nome: ")

if "silva" in nome.lower():
    print("Nome tem Silva.")
else:
    print("Nome não tem Silva.")
    