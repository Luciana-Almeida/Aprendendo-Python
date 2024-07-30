# Desafio 38: Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem: (a) o primeiro valor é maior; (b) o segundo valor é maior; (c) não existe valor maior, os dois são iguais.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}.")

elif n2 > n1:
    print(f"{n2} é maior que {n1}.")

else:
    print(f"{n1} é igual a {n2}.")
    