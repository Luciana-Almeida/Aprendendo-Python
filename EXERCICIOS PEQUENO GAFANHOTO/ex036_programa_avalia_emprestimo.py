# Desafio 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o seu salário: R$ "))
prazo_ano = int(input("Em quantos anos você quer financiar a compra? "))

prestacao_mes = valor_casa / (prazo_ano * 12)

print(f"Valor da prestação mensal: R$ {prestacao_mes:.2f}")

if prestacao_mes > (salario * 30) / 100:
    print("Seu impréstimo foi negado. Prestação mensal não pode exceder 30 por cento do seu salário.")

else:
    print("Empréstimo pode ser concedido. Nosso gerente vai entrar em contato com você.")
