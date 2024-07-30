# Desafio 42: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais; Isósceles: dois todos iguais; Escaleno: todos os lados diferentes.

a = input("Informe o comprimento do primeiro lado: ")
b = input("Informe o comprimento do segundo lado: ")
c = input("Informe o comprimento do terceiro lado: ")

if (a + b > c) and (a + c > b) and (b + c > a):
    print("As retas podem formar um triângulo.")

    if a == b == c:
        print("Todos os lados são iguais e formam um triângulo equilátero.")

    elif a == b or a == c or d == c:
        print("Dois lados são iguais e forma um triângulo isósceles.")

    elif a != b != c:
        print("Todos os lados são diferentes e formam um triângulo escaleno!")

else:
    print("As retas não podem formar um triângulo.")
    