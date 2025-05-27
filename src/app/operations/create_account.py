from .filter_customer import filter_customer
from app.account import CheckingAccount

def create_account(number_account, customers, accounts):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if not customer:    
        print("\n=== Cliente não encontrado, fluxo de criação de conta encerrado! ===")
        return

    account = CheckingAccount.new_account(customer=customer, number=number_account)
    accounts.append(account)
    customer.accounts.append(account)

    print("\n=== Conta criada com sucesso! ===")