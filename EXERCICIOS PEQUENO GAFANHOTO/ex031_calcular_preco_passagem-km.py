# Desafio 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km a R$0,45 para viagens mais longas.

distancia = float(input("Informe a distância (Km) até o destino: "))

if distancia < 200:
    preco = distancia * 0.50
    print(f"O valor da passagem é R$ {preco:.2f}.")
else:
    preco = distancia * 0.45
    print(f"O valor da passagem é R$ {preco:.2f}.")
