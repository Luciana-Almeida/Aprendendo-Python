#  Desenvolva um programa que leia o nome idade e sexo de 4 pessoas. No final do programa mostre: a) a média de idade do grupo; b) qual o nome do homem mais velho; c) quantas mulheres têm menos de 20 anos.

soma_idade = 0
idade_mulher = 0
idade_homem = 0

for i in range(1, 5):
    print(f"---------- {i}ª pessoa ----------")
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    sexo = input("Informe o sexo (M/F): ").strip().upper()

    soma_idade += idade

    if sexo == "F" and idade < 20:
        idade_mulher += 1

    if sexo == "M" and idade > idade_homem:
        idade_homem = idade
        nome_homem_mais_velho = nome

media_idade = soma_idade / i

print("---------- RESULTADO ----------")
print(f"A média de idade do grupo é {media_idade:.2f} anos.")
print(f"Existem {idade_mulher} mulheres com menos de 20 anos.")
print(f"O nome do homem mais velho é {nome_homem_mais_velho}.")
