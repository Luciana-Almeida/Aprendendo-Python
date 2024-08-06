# Leia um número inteiro e diga se ele é ou não um número primo

# Solicita ao usuário que insira um número inteiro
numero = int(input("Informe um número: "))

# Inicializa a variável para contar o número de divisores
total = 0

# Loop para verificar cada número de 1 até o número informado
for c in range(1, numero + 1):
    # Verifica se o número é divisível por c
    if numero % c == 0:
        # Imprime o número na cor azul se for divisível
        print("\033[34m", end=" ")
        # Incrementa o contador de divisores
        total += 1
    else:
        # Imprime o número na cor vermelha se não for divisível
        print("\033[31m", end=" ")
    # Imprime o número atual do loop
    print(f"{c}", end=" ")

# Pula uma linha e imprime o número de vezes que o número foi divisível
print(f"\nO número {numero} foi divisível {total} vezes.")

# Verifica se o número é primo (tem exatamente 2 divisores)
if total == 2:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
