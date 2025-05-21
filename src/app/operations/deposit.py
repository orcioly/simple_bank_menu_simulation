def deposit(balance, value, statement, /):

    if value > 0:
        balance += value
        statement += f"Depósito:\tR$ {value:.2f}\n"
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return balance, statement