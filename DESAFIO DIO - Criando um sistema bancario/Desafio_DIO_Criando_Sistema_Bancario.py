#Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0   #O sistema deve permitir realizar 3 saques diários 
LIMITE_SAQUES = 3   #O sistema deve ter um limite de até R$ 500,00 por saque

while True:
    
    opcao = input(menu)

    # Depósito: permitir apenas depósitos de valores positivos (considerar que a pessoa pode ter um saldo negativo); todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
    if opcao == "1":
        valor_deposito = input("Informe o valor que deseja depositar: R$ ")
        valor_deposito = valor_deposito.replace("." , "").replace("," , ".")
        valor_deposito = float(valor_deposito)

        if valor_deposito > 0:      #considerar valores positivos
            saldo += valor_deposito     #adicionar o valor depositado e somar ao saldo existente
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")


    # Saque: permitir até 3 saques diários; limite de R$ 500,00 por saque; caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo; todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
    elif opcao == "2":
        valor_saque = input("Informe o valor que deseja sacar: R$ ")
        valor_saque = valor_saque.replace(",", ".")
        valor_saque = float(valor_saque)

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite    

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Você atingiu o valor limite para saque.")

        elif excedeu_saques:
            print("Operação falhou! Você atingiu o limite de 3 saques diários.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")


    # Extrato: essa operação deve listar todos os depósitos e saques realizados na conta; no fim da listagem deve ser exibido o saldo atual da conta; os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=================================")


    elif opcao == "0":
        break


    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
        