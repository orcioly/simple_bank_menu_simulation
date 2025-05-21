def display_extract(balance, /, *, statement):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("==========================================")