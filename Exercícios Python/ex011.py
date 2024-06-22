#Crie um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendp que cada litro de tinta pinta uma área de 2 m2.
nome = input('Olá, qual o seu nome? ')
altura = input(f'{nome}, qual a altura da sua parede? ')
largura = input('E a largura? ')
#substitui vírgulas por ponto
altura = altura.replace(',' , '.')
largura = largura.replace (',' , '.')
#converter as strings em float
altura = float(altura)
largura = float(largura)
#calcular a área da parede
area = altura * largura
qtinta = area / 2
print(f'{nome}, sua parede tem uma área de {area:.2f} metros quadrados, serão necessários {qtinta:.2f} litros de tinta para pintá-la!')
