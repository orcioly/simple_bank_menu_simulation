from app.account import Transaction, Account

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def register(self, account: Account):
       success_transaction = account.deposity(self.value)

       if success_transaction:
           account.historical.add_transaction(self)
