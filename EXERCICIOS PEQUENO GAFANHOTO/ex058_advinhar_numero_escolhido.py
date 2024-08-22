# Desafio 28: Escreva um código que faça o computador "pensar" em um número inteiro entre 0 e 5 a peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Desafio 58: Melhore o desafio do Desafio 028 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

tentativas = 0

computador = randint(1, 10)
print("Escolhendo um número...")
sleep(1)
print("Já pensei em um número!")

jogador = int(input("Advinhe qual número eu pensei: "))

while jogador != computador:
    tentativas += 1
    if jogador > computador:
        print(f"Número errado! É um número menor que {jogador}")

    if jogador < computador:
        print(f"Número errado! É um número maior que {jogador}")
    
    jogador = int(input("Advinhe qual número eu pensei: "))

if jogador == computador:
    print(f"Você acertou depois de {tentativas} tentativas!")
