#  Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso.

pessoas_peso = []

for n in range(5):
    peso = float(input("Informe o peso em kg: "))
    pessoas_peso.append(peso)

maior_peso = max(pessoas_peso)
menor_peso = min(pessoas_peso)

print(f"O maior peso é Kg {maior_peso}, o menor peso é Kg {menor_peso}.")
