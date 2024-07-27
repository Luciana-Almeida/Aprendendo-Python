# Desafio 28: Escreva um código que faça o computador "pensar" em um número inteiro entre 0 e 5 a peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("Pensando...")
print("-=-" * 20)
sleep(3)
jogador = int(input("Em que número eu pensei? "))

if jogador == computador:
    print(f"Você acertou! O número escolhido foi {computador}!")
else:
    print(f"Você errou! O número escolhido foi {computador}!")

