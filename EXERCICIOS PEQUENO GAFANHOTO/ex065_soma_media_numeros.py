# Desafio 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitação de valores.

contador = 0
soma = 0
maior_valor = 0
menor_valor = 0
media = 0
# contador = soma = maior_valor = menor_valor = media = 0
sair = ""

while sair != "S":
    numero = int(input("Informe um número: "))
    contador += 1
    soma += numero
    
    if contador == 1:
        maior_valor = menor_valor = numero
    
    else:
        if numero > maior_valor:
            maior_valor = numero

        if numero < menor_valor:
            menor_valor = numero

    sair = input("Deseja encerrar (S/N)? ").upper().strip()[0]

media = soma / contador

print(f"Você digitou {contador} números.")
print(f"A média entre os valores é {media}.")
print(f"O maior valor é {maior_valor}.")
print(f"O menor valor é {menor_valor}.")
