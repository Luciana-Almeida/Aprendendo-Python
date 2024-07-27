# Desafio 33: Faça um programa que leia três números e mostre qual é o maior e qual o menor.

numeros = []

for i in range(3):
    numero = int(input("Informe um número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
