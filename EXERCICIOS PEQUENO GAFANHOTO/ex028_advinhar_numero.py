# Desafio 28: Escreva um código que faça o computador "pensar" em um número inteiro entre 0 e 5 a peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice 

numeros = [1, 2, 3, 4, 5]
numero_sorteado = choice(numeros)

numero = int(input("Advinhe qual o número escolhido: "))

if numero == numero_sorteado:
    print(f"Você acertou! O número escolhido foi {numero_sorteado}!")
else:
    print(f"Você errou! O número sorteado foi {numero_sorteado}!")

