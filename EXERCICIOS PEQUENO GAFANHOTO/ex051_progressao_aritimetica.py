# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Solicita o primeiro termo e a razão da PA
primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
decimo_termo = primeiro_termo + (10 - 1) * razao

# Exibe os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
for n in range(primeiro_termo, decimo_termo + razao, razao):
    print(n, end = " -> ")
