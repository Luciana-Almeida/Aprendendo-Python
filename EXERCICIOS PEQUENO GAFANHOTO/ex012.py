#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
import re

nome = input('Olá, qual o seu nome? ')
produto = input('Qual o produto que você gostaria de comprar com desconto? ')
valor = input('Qual o valor do produto? ')
# Remove o símbolo de moeda e pontos de separação de milhar
valor = re.sub(r'[R$\s]', ' ' , valor)
#substitui vírgula por ponto
valor = valor.replace('.', ' ').replace(',' , '.')
#converte valor en float
valor = float(valor)
#define taxa de desconto
taxa_desconto = 0.05
#calcula o valor do desconto
valor_desconto = valor * (1 - taxa_desconto)
print(f'{nome}, você ganhou 5% de desconto! Você pode comprar o produto {produto} por apenas {valor_desconto:.2f}! Posso enviar o link de pagamento para seu WhatsApp?')
