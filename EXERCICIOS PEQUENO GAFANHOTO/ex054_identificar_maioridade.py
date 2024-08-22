#  Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maioridade = 0
menoridade = 0

for n in range(7):
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    idade = date.today().year - ano_nascimento

    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f"{maioridade} pessoas já atingiram a maioridade.")        
print(f"{menoridade} pessoas ainda não atingiram a maioridade.")


