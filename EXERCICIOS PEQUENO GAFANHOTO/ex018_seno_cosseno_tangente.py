# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo

import math

angulo = float(input("Digite o valor do ângulo: "))
angulo_radiano = math.radians(angulo)

seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f"Estes são os valores do ângulo {angulo}: \n seno = {seno:.2f} \n cosseno = {cosseno:.2f} \n tangente = {tangente:.2f}")

#Estes são os valores do ângulo 21.0: 
 #seno = 0.36 
 #cosseno = 0.93 
 #tangente = 0.38
