# Desafio 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5x4x3x2x1 = 120 

# Solicitar ao usuário que informe o número
numero = int(input("Digite um número: "))

# Inicializar as variáveis
fatorial = 1
contador = numero

# Usar um loop while para calcular o fatorial
while contador > 1:  # Enquanto o contador for maior que 1
    fatorial *= contador  # Multiplica fatorial pelo valor do contador
    contador -= 1  # Diminui o contador em 1

# Mostrar o resultado
print(f"O fatorial de {numero} é {fatorial}")
