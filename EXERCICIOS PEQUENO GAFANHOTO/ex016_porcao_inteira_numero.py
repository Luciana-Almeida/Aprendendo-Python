# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira

from math import trunc

numero = float(input("Digite um valor: "))
numero_inteiro = trunc(numero)

print(f"A porção inteira de {numero} é {numero_inteiro}!")

