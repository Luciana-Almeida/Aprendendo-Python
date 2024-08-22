# Desafio 59: Crie um programa que leia dois valores e mostre um menu na tela: [1] Somar; [2] Multiplicar; [3] Maior, [4] Novos números; [5] Sair do programa. Seu programa deverá executar a operação escolhida em cada caso.

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("informe o segundo número: "))

while True:
    menu = """
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do programa
>>> Escolha uma opção: """

    opcao = int(input(menu))

    if opcao == 1:
        soma = numero_1 + numero_2
        print(f"A soma de {numero_1} + {numero_2} é {soma}.")

    elif opcao == 2:
        multiplicar = numero_1 * numero_2
        print(f"A multiplicação de {numero_1} x {numero_2} é {multiplicar}.")

    elif opcao == 3:
        if numero_1 > numero_2:
            print(f"{numero_1} é maior que {numero_2}.")
        
        elif numero_1 < numero_2:
            print(f"{numero_2} é maior que {numero_1}.")
        
        else:
            print("Os números são iguais.")

    elif opcao == 4:
        numero_1 = int(input("Informe o primeiro número: "))
        numero_2 = int(input("informe o segundo número: "))

    elif opcao == 5:
        break

    else:
        print("Opção inválida! Escolha uma opção no menu.")
