# Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5x4x3x2x1 = 120 

# Solicitar ao usuário que informe o número para calcular o fatorial
numero = int(input("Digite um número para calcular seu Fatorial: "))
contador = numero
fatorial = 1  # Inicializa fatorial como 1

# Iniciar a exibição da sequência do cálculo do fatorial
print(f'Calculando {numero}! = ', end='')

# Usar um loop while para calcular o fatorial
while contador > 0:
    print(f'{contador}', end='')
    fatorial *= contador  # Multiplica o valor atual de fatorial pelo contador
    
    print(' x ' if contador > 1 else ' = ', end='')  # Adiciona 'x' ou '=' dependendo do valor de contador
    contador -= 1  # Decrementa contador

# Mostrar o resultado final do fatorial
print(f'{fatorial}')
