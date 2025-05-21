from utils import menu
from operations import deposit, withdraw, display_extract, create_account, create_customer, list_accounts

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

if __name__ == "__main__":
    main()