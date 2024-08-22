# Desafio 63: Escreva um programa que leia um número “n” inteiro qualquer e mostre na tela os “n” primeiros elementos de uma sequência de Fibonacci. Ex: 0 -> 1 -> 1-> 2 -> 3 -> 5 -> 8.

# Perguntamos quantos números da sequência você quer ver
n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

# Começamos com os dois primeiros números da sequência
termo_1 = 0
termo_2 = 1

# Exibimos os primeiros dois números
print(f"{termo_1} -> {termo_2}", end="")

# Agora vamos calcular e mostrar os próximos números usando um loop
contador = 3  # Já mostramos os primeiros dois termos, então começamos o contador com 3

while contador <= n:
    termo_novo = termo_1 + termo_2  # Somamos os dois últimos termos para achar o próximo
    print(f" -> {termo_novo}", end="")  # Mostramos o novo termo
    termo_1 = termo_2  # Atualizamos o primeiro termo para ser o segundo
    termo_2 = termo_novo  # O segundo termo agora é o novo termo que achamos
    contador += 1  # Passamos para o próximo termo

print(" -> Fim")  # Mostramos que acabou
