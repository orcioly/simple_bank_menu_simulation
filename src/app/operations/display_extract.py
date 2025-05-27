from app.operations.filter_customer import filter_customer
from app.operations.recover_customer_account import recover_customer_account

def display_extract(customers):
    
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n=== Cliente não encontrado! ===")
        return
    
    account = recover_customer_account(customer)

    if not account:
        return

    print("\n================ EXTRATO ================")
    transactions = account.historical.transactions

    extract = ""
    if not transactions:
        extract = "Não foram realizadas movimentações."
    else:
        for transaction in transactions:
            extract += f"\n{transaction["tipo"]}:\n\tR$ {transaction["valor"]:.2f}"
            
    print(extract)
    print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
    print("==========================================")