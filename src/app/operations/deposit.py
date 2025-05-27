from app.customer import Customer
from app.account import Deposit
from .filter_customer import filter_customer
from .recover_customer_account import recover_customer_account

def deposit(customers: Customer):
    
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n=== Cliente não encontrado! ===")
        return
    
    value = float(input("Informe o valor do depósito: "))
    transaction = Deposit(value)  
    account = recover_customer_account(customer)

    if not account:
        return
    
    customer.perform_transaction(account, transaction)
    
