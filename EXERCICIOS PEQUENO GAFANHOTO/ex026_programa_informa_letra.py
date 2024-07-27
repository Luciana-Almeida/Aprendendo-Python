# Desafio 26: Crie um programa que leia uma frase e diga quantas vezes aparece a letra “A”, em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez.

nome = input("Informe o nome completo: ").srtip().lower()

print(f"A letra A aparece {nome.count("a")} vezes")
print(f"A letra A aparece pela primeira vez na posição {nome.find("a")}")
print(f"A letra A aparece pela última vez na posição {nome.rfind("a")}")
