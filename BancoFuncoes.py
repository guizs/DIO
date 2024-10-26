# Sistema Bancário Simples

# Dicionário para armazenar usuários
usuarios = {}
# Dicionário para armazenar contas
contas = {}

def menu():
    print("\n=== Sistema Bancário ===")
    print("1. Criar Usuário")
    print("2. Criar Conta")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Exibir Extrato")
    print("6. Listar Contas")
    print("7. Sair")

def criar_usuario(nome, cpf):
    if cpf not in usuarios:
        usuarios[cpf] = nome
        print(f"Usuário {nome} criado com sucesso!")
    else:
        print("Usuário já existe.")

def filtrar_usuario(cpf):
    return usuarios.get(cpf, None)

def criar_conta(cpf):
    if cpf in usuarios:
        conta_numero = len(contas) + 1
        contas[conta_numero] = {
            "usuario": usuarios[cpf],
            "saldo": 0,
            "extrato": []
        }
        print(f"Conta número {conta_numero} criada com sucesso!")
    else:
        print("Usuário não encontrado.")

def depositar(conta_numero, valor):
    if conta_numero in contas:
        contas[conta_numero]["saldo"] += valor
        contas[conta_numero]["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta_numero}.")
    else:
        print("Conta não encontrada.")

def sacar(conta_numero, valor):
    if conta_numero in contas:
        if valor <= contas[conta_numero]["saldo"]:
            contas[conta_numero]["saldo"] -= valor
            contas[conta_numero]["extrato"].append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta_numero}.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def exibir_extrato(conta_numero):
    if conta_numero in contas:
        print(f"\n=== Extrato da Conta {conta_numero} ===")
        for movimento in contas[conta_numero]["extrato"]:
            print(movimento)
        print(f"Saldo Atual: R$ {contas[conta_numero]['saldo']:.2f}")
    else:
        print("Conta não encontrada.")

def listar_contas():
    print("\n=== Listagem de Contas ===")
    for numero, conta in contas.items():
        print(f"Conta {numero}: Usuário {conta['usuario']} - Saldo: R$ {conta['saldo']:.2f}")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do Usuário: ")
            cpf = input("CPF do Usuário: ")
            criar_usuario(nome, cpf)
        elif opcao == "2":
            cpf = input("CPF do Usuário para criar a conta: ")
            criar_conta(cpf)
        elif opcao == "3":
            conta_numero = int(input("Número da conta para depósito: "))
            valor = float(input("Valor a depositar: "))
            depositar(conta_numero, valor)
        elif opcao == "4":
            conta_numero = int(input("Número da conta para saque: "))
            valor = float(input("Valor a sacar: "))
            sacar(conta_numero, valor)
        elif opcao == "5":
            conta_numero = int(input("Número da conta para exibir extrato: "))
            exibir_extrato(conta_numero)
        elif opcao == "6":
            listar_contas()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
