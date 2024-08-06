# Refaça o desafio 009, mostrando. A tabuada de um numero que o usuário escolher só que afora usando um laço for.

numero = int(input("Informe um número para calcular a tabuada: "))
print(f"A tabuada de {numero} é:")

for n in range(11):
    tabuada = numero * n
    print(f"{numero} x {n} = {tabuada}")
