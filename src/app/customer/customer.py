class Customer:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
      transaction.register(account)

    def add_account(self, account):
     self.accounts.append(account)