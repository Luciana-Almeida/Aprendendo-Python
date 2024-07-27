# Desafio 22: Crie um programa que leia o nome completo de uma pessoa e mostra:
    # O nome com todas as letras maiúsculas
    # O nome com todas minúsculas.
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.

nome = input("Informa o nome completo: ")
quantidade_letras = nome.replace(" " , "")
nome_separado = nome.split()

print(nome.upper())
print(nome.lower())
print(len(quantidade_letras))
print(len(nome_separado[0]))
