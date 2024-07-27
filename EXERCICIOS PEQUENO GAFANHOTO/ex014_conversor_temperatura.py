# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Solicita ao usuário para digitar a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura de Celsius para Fahrenheit usando a fórmula
fahrenheit = celsius * (9/5) + 32

# Imprime o resultado da conversão
print(f"{celsius} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit")
