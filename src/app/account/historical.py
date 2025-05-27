from datetime import datetime

class Historical:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions
    
    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "tipo": transaction.__class__.__name__,
                "valor": transaction.value,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
      
