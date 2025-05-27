from app.utils import menu
from app.operations import deposit, withdraw, display_extract, create_account, create_customer, list_accounts

def main():
    customers = []
    accounts = []

    while True:
        option_menu = menu()
        try:

            if option_menu == "d":
               deposit(customers)

            elif option_menu == "s":
                withdraw(customers)

            elif option_menu == "e":
                display_extract(customers)

            elif option_menu == "c":
                create_customer(customers)

            elif option_menu == "n":
                number_account = len(accounts) + 1
                create_account(number_account, customers, accounts)
            
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