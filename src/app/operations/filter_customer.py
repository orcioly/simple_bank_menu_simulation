from typing import List
from app.customer import PeoplePhysical

def filter_customer(cpf: str, customers: List[PeoplePhysical]):
    customers_filtered = [customer for customer in customers if customer.cpf == cpf]
    return customers_filtered[0] if customers_filtered else None