#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
nome = str(input('Qual o nome do aluno? '))
nota1 = float(input('Qual a nota da primeira prova? '))
nota2 = float(input('Qual a nota da segunda prova? '))
media = (nota1 + nota2)/2
print('A nota média do aluno {} é {:.2f}' .format(nome, media))
