#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA 
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = input("Informe uma frase: ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
