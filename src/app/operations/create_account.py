from .filter_customer import filter_customer

def create_account(agency, number_account, customers):
    cpf = input("Informe o CPF do cliente: ")
    customer = filter_customer(cpf, customers)

    if customer:    
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agency, "numero_conta": number_account, "cliente": customer}
    else:
        print("\nCliente não cadastrado!")