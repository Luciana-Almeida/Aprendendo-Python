#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
nome = str(input('Olá, qual o seu nome? '))
v = str(input('Qual o valor em metros que gostaria de converter? '))

# Substitui a vírgula por ponto
v = v.replace(',' , '.')

# Converte a string para float
v = float(v)

# Calcula centímetros e milímetros
cm = int(v * 100)
mm = int(v * 1000)

# Exibe os resultados
print('{}, {} metros equivale a: \n{} centímetros \n{} milímetros' .format(nome, v, cm, mm))
