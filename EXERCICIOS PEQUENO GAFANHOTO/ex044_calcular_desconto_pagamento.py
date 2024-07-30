# Desafio 44: Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:
# à vista, dinheiro ou chegue: 10% de desconto
# à vista no cartão: 5% de desconto
# Em 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input("Informe o valor do produto: R$ "))

menu = """
[1] À vista, dinheiro ou cheque
[2] À vista no cartão de crédito
[3] Parcelado no cartão de crédito em 2x
[4] Parcelado no cartão de crédito em 3x ou mais

Escolha a forma de pagamento: """

option = int(input(menu))

if option == 1:
    valor_pagar = valor - (valor * 0.1)
    print(f"Nesta forma de pagamento, o produto no valor de R$ {valor:.2f} terá um desconto de 10 por cento e você pagará R$ {valor_pagar:.2f}.")

elif option == 2:
    valor_pagar = valor - (valor * 0.05)
    print(f"Nesta forma de pagamento, o produto no valor de R$ {valor:.2f} terá um desconto de 5 por cento e você pagará R$ {valor_pagar:.2f}.")

elif option == 3:
    valor_pagar = (valor / 2)
    print(f"Você pode pagar o valor em 2x de R$ {valor_pagar:.2f}, sem juros no cartão.")

elif option == 4:
    valor_pagar = valor + (valor * 0.2)
    print(f"Nesta forma de pagamento você pode dividir o valor de R$ {valor:.2f} no cartão a partir de 3x, mas o valor será acrescido de 20 por cento de juros. Ao final você pagará R$ {valor_pagar:.2f}.")

else:
    print("Opção inválida! Escolha uma opção do menu.")
