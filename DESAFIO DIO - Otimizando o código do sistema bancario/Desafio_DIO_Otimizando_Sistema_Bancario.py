import textwrap

def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

# Função depositar
def depositar(saldo, valor, extrato, /):  # receber os argumentos apenas por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n== Depósito realizado com sucesso! ==")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        
    return saldo, extrato

# Função sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # receber argumentos apenas por nome
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
        
    elif excedeu_limite:
        print("\nOperação falhou. Você atingiu o valor limite para saque.")
        
    elif excedeu_saques:
        print("\nOperação falhou! Você atingiu o limite de três saques diários.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n== Saque realizado com sucesso! ==")
        
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques

# Função exibir_extrato
def exibir_extrato(saldo, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================")

# Função criar_usuario
def criar_usuario(usuarios):
    cpf = input("Informe o número do CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário cadastrado com este CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

# Função filtrar_usuario
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função criar_conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    return None

# Função listar_contas
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0   # O sistema deve permitir realizar 3 saques diários
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "1":  # Depositar
            valor = float(input("Informe o valor que deseja depositar R$: ")) 
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":  # Sacar
            valor = float(input("Informe o valor que deseja sacar: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == "3":  # Extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":  # Nova conta
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":  # Listar contas
            listar_contas(contas)

        elif opcao == "6":  # Novo usuário
            criar_usuario(usuarios)

        elif opcao == "0":  # Sair
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada")

main()
