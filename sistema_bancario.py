menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
numero_saques = 0
extrato = ""

LIMITE_VALOR_SAQUE = 500.00
LIMITE_QUANTIDADE_SAQUES = 3


def sacar(valor):

    global saldo, numero_saques, extrato

    if valor <= saldo and valor <= LIMITE_VALOR_SAQUE:
        numero_saques += 1
        saldo -= valor
        extrato += f"     Saque...: R$ {valor_saque:8.2f} -\n"
    else:
        if valor > saldo: 
            print(f"Saldo insuficiente")
        elif valor > LIMITE_VALOR_SAQUE:
            print(f"Limite do valor diário de saque excedido.  Limite R$ {LIMITE_VALOR_SAQUE:.2f}")
        else:
            print(f"Operação falhou! O valor informado não é válido")


def depositar(valor):

    global saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"     Depósito: R$ {valor:8.2f} +\n"
    else:
        print(f"Operação falhou! O valor <{valor}> é inválido")


while True:
    
    opcao = input(menu)

    if opcao == 'd':
        try:
            valor_deposito = float(input("Informe o valor do depósito: "))
        except ValueError: 
            print(f"Operação falhou! O valor informado não é válido")
        else:
            depositar(valor_deposito)

    elif opcao == 's':
        if numero_saques == LIMITE_QUANTIDADE_SAQUES:
            print(f"Você exceceu a quantidade de <{LIMITE_QUANTIDADE_SAQUES}> saques diários.")
        else:
            try:
                valor_saque = float(input("Informe o valor do saque: "))
            except ValueError: 
                print(f"Operação falhou! O valor informado não é válido")
            else:
                sacar(valor_saque)

    elif opcao == 'e':
        print("\n============ EXTRATO =============\n")
        print(extrato)
        print(f"     Saldo  => R$ {saldo:8.2f}\n")
        print("==================================")
        print(f"OBS: Foram feitos {numero_saques} saques hoje.")

    elif opcao == 'q':
        break

    else:
        print(f"Operação <{opcao}> inválida, por favor selecione novamente a operação desejada")