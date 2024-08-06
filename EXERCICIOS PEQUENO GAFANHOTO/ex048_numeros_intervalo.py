# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 e 500.

soma = 0    # Soma os valores
cont = 0    # Conta os valores

for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print(f"A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: {soma}.")

# para escrever um código mais eficiente escrever a função range com um passo 2
soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont += 1
        soma += numero

print(f"Foram encontrados {cont} números neste intervalo.\nA soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: {soma}.")

# Foram encontrados 83 números neste intervalo.
# A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: 20667.
