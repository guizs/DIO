class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def exibir_extrato(self):
        print(f"\n=== Extrato da Conta de {self.usuario.nome} ===")
        for movimento in self.extrato:
            print(movimento)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}

    def criar_usuario(self, nome, cpf):
        if cpf not in self.usuarios:
            self.usuarios[cpf] = Usuario(nome, cpf)
            print(f"Usuário {nome} criado com sucesso!")
        else:
            print("Usuário já existe.")

    def criar_conta(self, cpf):
        usuario = self.usuarios.get(cpf)
        if usuario:
            conta = Conta(usuario)
            conta_numero = len(self.contas) + 1
            self.contas[conta_numero] = conta
            print(f"Conta número {conta_numero} criada com sucesso!")
        else:
            print("Usuário não encontrado.")

    def depositar(self, conta_numero, valor):
        conta = self.contas.get(conta_numero)
        if conta:
            conta.depositar(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta_numero}.")
        else:
            print("Conta não encontrada.")

    def sacar(self, conta_numero, valor):
        conta = self.contas.get(conta_numero)
        if conta:
            conta.sacar(valor)
            if valor <= conta.saldo:
                print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta_numero}.")
        else:
            print("Conta não encontrada.")

    def exibir_extrato(self, conta_numero):
        conta = self.contas.get(conta_numero)
        if conta:
            conta.exibir_extrato()
        else:
            print("Conta não encontrada.")

    def listar_contas(self):
        print("\n=== Listagem de Contas ===")
        for numero, conta in self.contas.items():
            print(f"Conta {numero}: Usuário {conta.usuario.nome} - Saldo: R$ {conta.saldo:.2f}")


def menu():
    print("\n=== Sistema Bancário ===")
    print("1. Criar Usuário")
    print("2. Criar Conta")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Exibir Extrato")
    print("6. Listar Contas")
    print("7. Sair")


def main():
    banco = Banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do Usuário: ")
            cpf = input("CPF do Usuário: ")
            banco.criar_usuario(nome, cpf)
        elif opcao == "2":
            cpf = input("CPF do Usuário para criar a conta: ")
            banco.criar_conta(cpf)
        elif opcao == "3":
            conta_numero = int(input("Número da conta para depósito: "))
            valor = float(input("Valor a depositar: "))
            banco.depositar(conta_numero, valor)
        elif opcao == "4":
            conta_numero = int(input("Número da conta para saque: "))
            valor = float(input("Valor a sacar: "))
            banco.sacar(conta_numero, valor)
        elif opcao == "5":
            conta_numero = int(input("Número da conta para exibir extrato: "))
            banco.exibir_extrato(conta_numero)
        elif opcao == "6":
            banco.listar_contas()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()