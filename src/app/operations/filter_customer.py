def filter_customer(cpf, customers):
    customers_filtered = [customer for customer in customers if customer["cpf"] == cpf]
    return customers_filtered[0] if customers_filtered else None