# Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores “M” ou “F”. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ""

# Loop até obter uma entrada válida
while sexo != "M" and sexo != "F":
    sexo = input("Informe o sexo (M/F): ").strip().upper()[0]
    if sexo != "M" and sexo != "F":
        print("Entrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")

# Saída ao obter uma entrada válida
print(f"Sexo '{sexo}' registrado com sucesso!")
