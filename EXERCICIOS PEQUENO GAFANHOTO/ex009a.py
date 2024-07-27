#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
nome = input('Olá, qual o seu nome? ')
v = int(input('De qual número você gostaria de ver a tabuada? '))
print(f'{nome}, a tabuada de {v} é:')
for i in range(11):
    print(f'{v} * {i} = {v * i}')
