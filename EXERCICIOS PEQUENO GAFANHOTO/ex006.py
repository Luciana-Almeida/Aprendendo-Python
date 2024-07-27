#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
print('O número é {}. \nSeu dobro é {}. \nO triplo é {}. \nE a sua raiz quadrada é {:.2f}!' . format(n, (n * 2), (n * 3), (n ** (1/2))))
