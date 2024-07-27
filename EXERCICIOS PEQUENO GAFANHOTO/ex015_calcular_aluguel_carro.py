# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input("informe a quantidade de km percorridos: "))
dias_aluguel = int(input("informa a quantidade de dias de aluguel: "))

valor_aluguel = (km_percorrido * 0.15) + (dias_aluguel * 60)

print(f"O valor a pagar pela locação é {valor_aluguel}")
