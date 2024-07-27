# Desafio 29: Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite.

velocidade = float(input("Informe a velocidade do veículo em km/h: "))
valor_multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"O veículo estava acima da velocidade permitida de 80 km/h.\nO valor da multa é R$ {valor_multa:.2f}.")

else:
    print("O veículo estava na velocidade permitida e não será multado.")
