# Desafio 27: Crie um programa que leia um nome completo de uma pessoa e em seguida mostre o primeiro e o último nome separado.

nome = input("Informe o nome: ").strip()
partes_nome = nome.split()

primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]

print("Muito prazer em te conhecer!")
print(f"O primeiro nome é {primeiro_nome.capitalize()}")
print(f"O último nome é {ultimo_nome.capitalize()}")
