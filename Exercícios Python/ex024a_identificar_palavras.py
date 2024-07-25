# Desafio 24: Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com a palavra “Santo”.

nome_cidade = input("Informe o nome da cidade: ").strip()

# lower() - Converte toda a string para letras minúsculas para garantir uma comparação consistente.

# startswith() - Verifica se a string começa com a substring especificada.

if nome_cidade.lower().startswith("santo"):
    print("Nome da cidade começa com Santo")
else:
    print("Nome não começa com Santo")
