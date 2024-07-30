# Desafio 37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: (1) para binário; (2) para octal; (3) para hexadecimal.

valor = int(input("Informe um número: "))

menu = """
[1] Binário
[2] Octal
[3] Hexadecimal
\033[1mEscolha a base de conversão\033[1m: """

option = input(menu)

if option == "1":
    binario = bin(valor)[2:]    #Fatiamento da string para remover os dois digitos iniciais do código
    print(f"{valor} convertido para binário é {binario}.")

elif option == "2":
    octal = oct(valor)[2:]
    print(f"{valor} convertido para octal é {octal}.")

elif option == "3":
    hexadecimal = hex(valor)[2:]
    print(f"{valor} convertido para hexadecimal é {hexadecimal}.")

else:
    print("Opção inválida. Escolha uma opção do menu.")
