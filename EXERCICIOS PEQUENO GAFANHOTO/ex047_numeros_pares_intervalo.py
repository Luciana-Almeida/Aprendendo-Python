# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Este laço executa duas verificações
for numero in range(1, 51):
    if numero % 2 == 0:
        print(numero, end=" ")


# Para escrever um código de forma mais eficiente e que mostre todos os números pares entre 1 e 50, você pode simplificar o loop usando a função range() com um passo de 2. Isso elimina a necessidade de verificar cada número com uma condição if, pois o próprio range já pode gerar apenas os números pares.

for numero in range(2, 51, 2):
    print(numero, end=" ")
