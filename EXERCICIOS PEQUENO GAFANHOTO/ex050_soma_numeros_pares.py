# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input(f"Informe o {c} número: "))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f"Você informou {cont} números pares.\nA soma destes números pares é {soma}!")
