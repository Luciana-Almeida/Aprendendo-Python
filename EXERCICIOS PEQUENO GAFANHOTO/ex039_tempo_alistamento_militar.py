# Desafio 39: Faça um programa que leia o ano do nascimento de um jovem e informa, de acordo com sua idade: (a) Se ele ainda vai se alistar ao serviço militar; (b) Se é a hora de se alistar; (c) Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Informe o ano de seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f"Você tem {idade} anos e precisa se alistar no serviço militar agora.")

elif idade < 18:
    tempo = 18 - (idade)
    print(f"Você tem {idade} anos. Ainda faltam {tempo} anos para você se alistar no serviço militar.")

elif idade > 18:
    tempo = (idade) - 18
    print(f"Você tem {idade} anos. Você precisa regularizar sua situação, pois deveria ter se alistado no serviço militar há {tempo} anos!")
