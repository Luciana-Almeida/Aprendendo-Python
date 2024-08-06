# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

print(emoji.emojize("Iniciando a contagem regressiva... ⏳"))

for cont in range(10, -1, -1): # Início, fim e step
    print(cont)
    sleep(1)
print(emoji.emojize("Fim da contagem regressiva! 💥"))
