
import textwrap
from abc import ABC, abstractmethod

# Classe abstrata que define um contrato para transações
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Deposito que herda de Transacao e implementa o método registrar
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

# Classe Saque que herda de Transacao e implementa o método registrar
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if 0 < self.valor <= conta._saldo and conta._numero_saques < Conta.LIMITE_SAQUES:
            conta._saldo -= self.valor
            conta._numero_saques += 1
            conta.historico.adicionar_transacao(self)
            return True
        return False

# Classe Historico que armazena as transações da conta
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Classe Conta que representa uma conta bancária
class Conta:
    LIMITE_SAQUES = 3  # Limite de saques diários

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._numero_saques = 0
        self._limite = 500

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedades para acessar os atributos privados
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @property
    def numero_saques(self):
        return self._numero_saques

    @numero_saques.setter
    def numero_saques(self, valor):
        self._numero_saques = valor

    @property
    def limite(self):
        return self._limite

    # Método para realizar um depósito
    def depositar(self, valor):
        transacao = Deposito(valor)
        if transacao.registrar(self):
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Método para realizar um saque
    def sacar(self, valor):
        if valor > self._limite:
            print("Operação falhou! O valor do saque excede o limite permitido.")
        elif self._numero_saques >= Conta.LIMITE_SAQUES:
            print("Operação falhou! Você atingiu o limite de saques diários.")
        else:
            transacao = Saque(valor)
            if transacao.registrar(self):
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! Verifique o valor do saque e saldo disponível.")

    # Método para imprimir o extrato da conta
    def extrato(self):
        print("\n============ EXTRATO ============")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                if isinstance(transacao, Deposito):
                    print(f"Depósito: R$ {transacao.valor:.2f}")
                elif isinstance(transacao, Saque):
                    print(f"Saque: R$ {transacao.valor:.2f}")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("\n=================================")

# Classe ContaCorrente que herda de Conta e redefine o limite
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite):
        super().__init__(numero, cliente)
        self._limite = limite

# Classe Cliente que gerencia as contas e realiza transações
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    # Método para realizar uma transação em uma conta
    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)

    # Método para adicionar uma conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica que herda de Cliente e adiciona informações específicas
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Função depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n== Depósito realizado com sucesso! ==")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
        
    return saldo, extrato

# Função sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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

# Função menu
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

# Função principal
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
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

if __name__ == "__main__":
    main()

