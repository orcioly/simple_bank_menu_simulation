from .account import Account
from .withdraw import Withdraw

class CheckingAccount(Account):
    def __init__(self, number, customer, limit=500, withdrawal_limit=3):
        super().__init__(number, customer)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, value):
        number_of_withdrawals = len([transaction for transaction in self.historical.transactions if transaction["tipo"] == Withdraw.__name__])

        exceeded_limit = value > self.limit
        exceeded_withdrawal = number_of_withdrawals >= self.withdrawal_limit

        if exceeded_limit:
            print("\n=== Operação falhou! O valor do saque excede o limite. ===")

        elif exceeded_withdrawal:
            print("\n=== Operação falhou! Número máximo de saques excedido. ===")

        else:
            return super().withdraw(value)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agency}
            C/C:\t{self.number}
            Titular:\t{self.customer.name}
        """