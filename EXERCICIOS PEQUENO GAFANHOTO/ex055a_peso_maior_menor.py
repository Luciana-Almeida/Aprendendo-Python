# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso.

# Inicializando as variáveis para armazenar o maior e menor peso
maior_peso = 0
menor_peso = float('inf')  # Um valor inicial muito alto

# Loop para ler os pesos
for p in range(5):
    peso = float(input(f"Informe o peso da {p}ª em kg: "))
    
    # Atualiza o maior e menor peso conforme necessário
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

# Imprime os resultados finais
print(f"O maior peso é Kg {maior_peso}, o menor peso é Kg {menor_peso}.")
