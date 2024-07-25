# Um professor quer sortear um de seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido

import random

menu = """
[1] Inserir aluno
[2] Sortear aluno
[3] Limpar lista de alunos
[4] Listar alunos
[5] Sair
Escolha a opção do menu: """

alunos = []

while True:
    opcao = input(menu)

    if opcao == "1":
        aluno = input("Insira o nome do aluno: ")
        alunos.append(aluno)

    elif opcao == "2":
        if alunos:
            aluno_sorteado = random.choice(alunos)
            print(f"@@@ O aluno sorteado foi {aluno_sorteado} @@@")
        else:
            print("A lista de alunos está vazia, por favor insira os nomes dos alunos.")
    
    elif opcao == "3":
        alunos.clear()
        print("A lista de alunos foi limpa.")

    elif opcao == "4":
        if alunos:
            print("Lista de alunos:")
            for aluno in alunos:
                print(aluno)
        
        else:
            print("A lista de alunos está vazia.")

    elif opcao == "5":
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida no menu.")
