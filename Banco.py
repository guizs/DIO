saldo = 0
extrato = []

def ver_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

def sacar(valor):
    global saldo
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def ver_extrato():
    print("\nExtrato:")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação registrada.")
    ver_saldo()

# Menu interativo
while True:
    print("\nBem-vindo ao Banco! Escolha uma opção:")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver Extrato")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        ver_saldo()
    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: R$ "))
        depositar(valor)
    elif opcao == "3":
        valor = float(input("Digite o valor para saque: R$ "))
        sacar(valor)
    elif opcao == "4":
        ver_extrato()
    elif opcao == "5":
        print("Obrigado por usar o Banco! Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
