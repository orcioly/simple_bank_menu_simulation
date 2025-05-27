from app.operations.recover_customer_account import recover_customer_account
from app.operations.filter_customer import filter_customer
from app.account import Withdraw

def withdraw(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n=== Cliente não encontrado! ===")
        return
    
    value = float(input("Informe o valor do saque: "))
    transaction = Withdraw(value)  
    account = recover_customer_account(customer)

    if not account:
        return
    
    customer.perform_transaction(account, transaction)