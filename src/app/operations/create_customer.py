from .filter_customer import filter_customer

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