# Desafio 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula seu IMC a mostra sou status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 a 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Informe o seu peso em Kg: "))
altura = float(input("Informe sua altura: "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}. Você está abaixo do peso!")

elif 18.5 <= imc < 25:
    print(f"Seu IMC é de {imc:.2f}. Você está no seu peso ideal!")

elif 25 <= imc < 30:
    print(f"Seu IMC é de {imc:.2f}. Você está com sobrepeso.")

elif 30 <= imc < 40:
    print(f"Seu IMC é de {imc:.2f}. Você está obeso!")

else:
    print(f"Seu IMC é de {imc:.2f}. Você está na faixa de obesidade mórbida! Consulte um médico!")

print("Procure um nutricionista para saber como manter uma dieta balanceada!")
