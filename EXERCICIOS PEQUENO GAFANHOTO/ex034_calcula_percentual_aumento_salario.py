# Desafio 34: Escreva um programa que pergunte o salário de um Funcionário e calcula o valor do seu aumento. Para salários superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_str = input("Informe o valor do salário: R$ ").replace(".", "").replace(",", ".")
salario = float(salario_str)

if salario > 1250.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O salário com aumento será de R$ {novo_salario:.2f}")
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"O salário com aumento será de R$ {novo_salario:.2f}")
