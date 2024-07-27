# Desafio 32: Faça um programa que leia um ano qualquer a mostra se o ano é BISSEXTO.

from datetime import date

ano = int(input("Informe o ano para saber se ele é bissexto.\nColoque zero, se quiser saber se o ano atual é bissexto.\nAno: "))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")

else:
    print(f"O ano {ano} não é bissexto.")
