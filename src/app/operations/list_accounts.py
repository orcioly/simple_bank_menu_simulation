def list_accounts(accounts):
    for account in accounts:
        line= f"""\
            Agência:\t{account["agencia"]}
            C/C\t\t{account["numero_conta"]}
            Titular:\t{account["cliente"]["nome"]}
        """
        print("=" * 100)
        print(line)