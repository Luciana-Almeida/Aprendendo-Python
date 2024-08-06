# Desafio 45: Crie um programa que faça o computador jogar jokenpô com você

from random import choice
import emoji
from time import sleep

# Iniciando o jogo
print(emoji.emojize('Vamos jogar jokenpô :thumbs_up:'))

# Computador faz sua escolha
opcoes = ["Pedra", "Papel", "Tesoura"]
computador = choice(opcoes)

# Opções para o jogador escolher
menu = """
[1] Pedra 
[2] Papel   
[3] Tesoura
Escolha uma das opções: """

jogador = int(input(menu))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)

print("-=" * 15)
# Opção de escolha inválida
if jogador not in [1, 2, 3]:
    print("Escolha inválida! Tente novamente.")

else:
    # Mapear a escolha do jogador para o nome correspondente
    jogador_opcao = opcoes[jogador - 1]

    print(f"O computador escolheu {computador}!")
    print(f"Você escolheu {jogador_opcao}!")

    # Determinar o vencedor
    if computador == jogador_opcao:
        print("== Empate! ==")

    elif (computador == "Pedra" and jogador_opcao == "Tesoura") or \
         (computador == "Papel" and jogador_opcao == "Pedra") or \
         (computador == "Tesoura" and jogador_opcao == "Papel"):
        print("@@ O computador venceu! @@")
        
    else:
        print("## Você venceu! ##")

print("-=" * 15)
