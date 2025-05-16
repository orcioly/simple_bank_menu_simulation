balance = 0
limit = 500
statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

customer_name = input("Informe seu primeiro nome: ")

def menu():
    print("\n******************* MENU BANCÁRIO *******************\n")
    print(f"CLIENTE: {customer_name.title()}\n")
    print("Selecione a operação desejada:\n")
    print("D - Depositar")
    print("S - Sacar")
    print("E - Extrato")
    print("Q - Sair")


while True:
    menu()
    try:
        option = input("\nEscolha uma opção: ").lower()

        if option == "d":
            value = float(input("Informe o valor do depósito: "))

            if value > 0:
                balance += value
                statement += f"Depósito: R$ {value:.2f}\n"

            else:
                print("\nOperação falhou! O valor informado é inválido.")

        elif option == "s":
            value = float(input("Informe o valor do saque: "))

            exceeded_balance = value > balance

            exceeded_limit = value > balance

            exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

            if exceeded_balance:
                print("\nOperação falhou! Você não tem saldo suficiente.")

            elif exceeded_limit:
                print("\nOperação falhou! O valor do saque excede o limite.")

            elif exceeded_withdrawals:
                print("\nOperação falhou! Número máximo de saques excedido.")

            elif value > 0:
                balance -= value
                statement += f"Saque: R$ {value:.2f}\n"
                number_of_withdrawals += 1

            else:
                print("\nOperação falhou! O valor informado é inválido.")

        elif option == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not statement else statement)
            print(f"\nSaldo: R$ {balance:.2f}")
            print("==========================================")

        elif option == "q":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

    except ValueError:
        print("\nEntrada inválida, preencha os campos corretamente!")