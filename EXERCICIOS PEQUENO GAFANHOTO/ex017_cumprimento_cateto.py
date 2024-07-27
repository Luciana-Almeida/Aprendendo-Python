# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt, hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

#soma_catetos = ((cateto_oposto ** 2) + (cateto_adjacente ** 2))
#hipotenusa = sqrt(soma_catetos)

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"O valor da hipotenusa é {hipotenusa:.2f}!")
