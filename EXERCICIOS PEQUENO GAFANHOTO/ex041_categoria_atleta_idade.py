# Desafio 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento do um atleta a mostra sua categoria, do acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SENIOR
# Acima: MASTER

from datetime import date

ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year

print("A categoria do atleta é:")

if ano_atual - ano_nascimento <= 9:
    print("MIRIM")

elif ano_atual - ano_nascimento <= 14:
    print("INFANTIL")

elif ano_atual - ano_nascimento <= 19:
    print("JUNIOR")

elif ano_atual - ano_nascimento <= 20:
    print("SENIOR")

else:
    print("MASTER")
