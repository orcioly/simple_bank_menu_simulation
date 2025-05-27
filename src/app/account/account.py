from .historical import Historical

class Account:
    def __init__(self, number, customer):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._customer = customer
        self._historical = Historical()

    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)

    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self._number
    
    @property
    def agency(self):
        return self._agency
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def historical(self):
        return self._historical
    
    def withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n=== Operação falhou! Você não tem saldo suficiente! ===")

        elif value > 0:
            self._balance -= value
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\nOperação falhou! O valor informado é inválido. ===")

        return False
    
    def deposity(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Depósito realizado com sucesso! ===")
            
        else:
            print("\n=== Operação falhou! O valor informado é inválido. ===")
        
        return True