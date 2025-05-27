from app.operations.filter_customer import filter_customer
from app.operations.recover_customer_account import recover_customer_account

LANGUAGE = {
    "Deposit": "Depósito",
    "Withdraw": "Saque"
}

def display_extract(customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n=== Cliente não encontrado! ===")
        return
    
    account = recover_customer_account(customer)

    if not account:
        print("\n=== Conta não encontrada! ===")
        return

    transactions = account.historical.transactions

    print("\n================ EXTRATO ================")
    if not transactions:
        print("Não foram realizadas movimentações.")
    else:
        for transaction in transactions:
            language_pt = LANGUAGE.get(transaction["tipo"], transaction["tipo"])
            print(f"\n{language_pt}:")
            print(f"\tR$ {transaction['valor']:.2f} - {transaction['data']}")

    print(f"\nSaldo:\n\tR$ {account.balance:.2f}")
    print("==========================================")
