def recover_customer_account(customer):
    if not customer.accounts:
        print("\n=== Cliente não possui conta! ===")
        return
    
    return customer.accounts[0]