#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
import re
nome = input('Qual o seu nome? ')
funcao = input(f'{nome}, Qual a sua função atual? ')
salario = input('Qual o seu salário atual? ')
# Remove o símbolo de moeda e pontos de separação de milhar
salario = re.sub(r'[R$\s]' , '', salario)
#substitui vírgula por ponto
salario = salario.replace('.' , '').replace(',' , '.')
#converte valor en float
salario = float(salario)
#define taxa de aumento
taxa_aumento = 0.15
#calcular o valor do aumento
salario_aumento = salario * (1 + taxa_aumento)
print(f'{nome}, quando você for promovido(a), você vai receber um salário de R$ {salario_aumento:.2f}!')
