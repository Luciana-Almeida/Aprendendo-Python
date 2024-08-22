# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso.

# Inicializando as variáveis para armazenar o maior e menor peso
maior_peso = 0
menor_peso = 0

# Loop para ler os pesos
for p in range(1, 6):
    peso = float(input(f"Informe o peso da {p}ª pessoa em kg: "))

    if p == 1:
        maior_peso = peso
        menor_peso = peso

    else:
        # Atualiza o maior e menor peso conforme necessário
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

# Imprime os resultados finais
print(f"O maior peso é {maior_peso} Kg, o menor peso é {menor_peso} Kg.")
