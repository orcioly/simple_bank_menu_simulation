def menu():
    print("\n******************* MENU BANCÁRIO *******************\n")
    print("Selecione a operação desejada:\n")
    print("D - Depositar")
    print("S - Sacar")
    print("E - Extrato")
    print("N - Nova conta")
    print("L - Listar contas")
    print("C - Novo cliente")
    print("Q - Sair")

    return input("\nDigite uma opção: ").lower()