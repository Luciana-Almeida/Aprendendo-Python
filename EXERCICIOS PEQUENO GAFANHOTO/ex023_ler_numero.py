# Desafio 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

numero = input("Informe um número entre 0 e 9999: ")
numero_digitos = numero.zfill(4)    # Adicionar zeros à esquerda, se necessário

print(f"Unidade: {numero_digitos[3]}")
print(f"Dezena: {numero_digitos[2]}")
print(f"Centena: {numero_digitos[1]}")
print(f"Milhar: {numero_digitos[0]}")
