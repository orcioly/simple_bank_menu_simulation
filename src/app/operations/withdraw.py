def withdraw(*, balance, value, statement, limit, number_of_withdrawals, withdrawal_limit):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = number_of_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif exceeded_withdrawals:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif value > 0:
        balance -= value
        statement += f"Saque:\t\tR$ {value:.2f}\n"
        number_of_withdrawals += 1

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return balance, statement