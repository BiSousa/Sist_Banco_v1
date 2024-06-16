menu = """

[0] - Depositar
[1] - Sacar
[2] - Extrato
[3] - Sair

--> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao ==  "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não é possível realizar o depósito!")
    elif opcao == "1":
        valor = float(input("Informe o valor que deseja sacar: "))

        if valor > saldo:
            print("Operação inválida. Saldo insuficiente.")
        elif valor > limite:
            print("Falha na operação. O valor é maior que o limite.")
        elif numero_saques >= limite_saques:
            print("Limite de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação inválida. O valor não é válido.")
    elif opcao == "2":
        print("----------EXTRATO----------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("---------------------------")
    elif opcao == "3":
        print("Até a próxima operação!")
        break
    else:
        print("Operação inválida. Insira uma operação válida!")