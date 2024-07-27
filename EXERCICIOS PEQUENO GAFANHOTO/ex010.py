#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar
nome = input('Olá, qual o seu nome? ')
vr = input('Qual o valor em real que você gostaria de converter para dólar? R$ ')

# Substitui a vírgula por ponto
vr = vr.replace(',' , '.')

# Converte a string para float
vr = float(vr)

# Converte reais para dólares
vd = float(vr / 3.27)
print(f'{nome}, com R${vr} reais você pode comprar US${vd:.2f} dólares')
