# Desafio 40: Crie um programa que leia duas notas de um aluno o calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida: (a) Média abaixo de 5.0: REPROVADO; (b) Média entre 5.0 a 5.9: RECUPERAÇÃO; (c) Média 7.0 ou superior: APROVADO

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media < 5:
    print(f"Sua nota média é {media:.2f}. Você está REPROVADO!")

elif 5.9 >= media >= 5:
    print(f"Sua nota média é {media:.2f}. Você está na RECUPERAÇÃO!")

else:
    print(f"Sua nota média é {media:.2f}. Parabéns! Você está APROVADO!")
