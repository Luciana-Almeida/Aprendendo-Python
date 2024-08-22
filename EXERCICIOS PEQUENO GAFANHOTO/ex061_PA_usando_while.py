# Desafio 61: Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Solicita o primeiro termo e a razão da PA
primeiro_termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

contador = 1
termo_atual = primeiro_termo

while contador <= 10:
    print(f"{contador}º termo: {termo_atual}")
    termo_atual += razao
    contador += 1
