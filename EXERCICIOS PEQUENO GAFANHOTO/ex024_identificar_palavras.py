# Desafio 24: Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com a palavra “Santo”.


nome_cidade = input("Informe o nome da cidade: ").strip().lower()
nome_fatiado = nome_cidade.split()

if nome_fatiado[0] == "santo":
    print("Nome da cidade começa com Santo")
else:
    print("Nome não começa com Santo")
