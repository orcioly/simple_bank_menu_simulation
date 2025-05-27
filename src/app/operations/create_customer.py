from .filter_customer import filter_customer
from app.customer import PeoplePhysical

def create_customer(customers):
    cpf = input("Informe o CPF (somente o CPF): ")
    customer = filter_customer(cpf, customers)

    if customer:    
        print("\n=== Já existe cliente com esse CPF! ===")
        return

    name = input("Informe o nome completo: ")
    date_of_birth = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, número, bairro, cidade): ")

    customer = PeoplePhysical(name=name, date_of_birth=date_of_birth, cpf=cpf, address=address)
    customers.append(customer)

    print("\n=== Conta criada com sucesso! ===")