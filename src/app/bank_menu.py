def menu():
    print("\n******************* MENU BANCÁRIO *******************\n")
    print("Selecione a operação desejada:\n")
    print("D - Depositar")
    print("S - Sacar")
    print("E - Extrato")
    print("N - Nova conta")
    print("L - Listar contas")
    print("C - Novo cliente")
    print("Q - Sair")

    return input("\nDigite uma opção: ").lower()

def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement += f"Depósito:\tR$ {value:.2f}\n"
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return balance, statement

def withdraw(*, balance, value, statement, limit, number_of_withdrawals, withdrawal_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_of_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif exceeded_withdrawals:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif value > 0:
        balance -= value
        statement += f"Saque:\t\tR$ {value:.2f}\n"
        number_of_withdrawals += 1

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return balance, statement

def display_extract(balance, /, *, statement):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("==========================================")

def filter_customer(cpf, customers):
    customers_filtered = [customer for customer in customers if customer["cpf"] == cpf]
    return customers_filtered[0] if customers_filtered else None

def create_customer(customers):
    cpf = input("informe o CPF (Apenas números): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\nJá existe usuário com esse CPF!")
        return

    name = input("Informe o nome completo: ")
    date_of_birth = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, número - bairro - cidade/uf): ")

    customers.append({"nome": name, "data_nascimento": date_of_birth, "cpf": cpf, "endereco": address})

    print("\n=== Usuário criado com sucesso! ===")

def create_account(agency, number_acccount, customers):
    cpf = input("Informe o CPF do usuário: ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agency, "numero_conta": number_acccount, "usuario": customer}
    else:
        print("\nUsuário não cadastrado!")

def list_accounts(accounts):
    for account in accounts:
        line= f"""\
            Agência:\t{account["agencia"]}
            C/C\t\t{account["numero_conta"]}
            Titular:\t{account["usuario"]["nome"]}
        """
        print("=" * 100)
        print(line)


def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    statement = ""
    number_of_withdrawals = 0
    customers = []
    accounts = []

    while True:
        option_menu = menu()
        try:

            if option_menu == "d":
                value = float(input("Informe o valor do depósito: "))

                balance, statement = deposit(balance, value, statement)

            elif option_menu == "s":
                value = float(input("Informe o valor do saque: "))

                balance, statement = withdraw(balance=balance, value=value, statement=statement, limit=limit, number_of_withdrawals=number_of_withdrawals, withdrawal_limit=WITHDRAWAL_LIMIT)

            elif option_menu == "e":
                display_extract(balance, statement=statement)

            elif option_menu == "c":
                create_customer(customers)

            elif option_menu == "n":
                number_account = len(accounts) + 1
                account = create_account(AGENCY, number_account, customers)

                if account:
                    accounts.append(account)
            
            elif option_menu == 'l':
                list_accounts(accounts)

            elif option_menu == "q":
                break

            else:
                print("\nOperação inválida, por favor selecione novamente a operação desejada.")

        except ValueError:
            print("\nEntrada inválida, preencha os campos corretamente!")

main()