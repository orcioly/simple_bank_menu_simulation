# 🏦 Menu Bancário em Python - Versão 3

Um projetinho **simples e direto** feito para quem está começando no mundo da programação. Essa versão foi refatorada utilizando classes com POO.

Essa aplicação simula um **menu bancário básico**, onde você pode **depositar**, **sacar**, **ver seu extrato**, **cadastrar cliente**, **cadastrar conta**, **listar contas** ou **sair do sistema**.

A ideia aqui é mostrar o básico de Python com **entrada de dados**, **estrutura de repetição**, **condicionais** e **manipulação de variáveis**. Nada de frameworks, nada de firula — é o Python raiz 🐍.

## 🚀 Funcionalidades

- Depósito de valores

- Saque com verificação de saldo, limite e número de saques

- Extrato com histórico de movimentações

- Menu interativo em loop

- Verificação de entrada inválida

- Cadastrar cliente

- Cadastrar conta

- Listar contas

## 📁 Estrutura do Projeto

```
project/
└── src/
    └── app/
        └── main.py
        └── account
        |    └── __init__.py
        |    └── account.py
        |    └── checking_account.py
        |    └── deposit.py
        |    └── historical.py
        |    └── transaction.py
        |    └── withdraw.py
        └── customer
        |    └── __init__.py
        |    └── customer.py
        |    └── people_physical.py
        └── operations
        |    └── __init__.py
        |    └── create_account.py
        |    └── create_customer.py
        |    └── deposit.py
        |    └── display_extract.py
        |    └── filter_customer.py
        |    └── list_accounts.py
        |    └── recover_customer_account.py
        |    └── withdraw.py
        └── utils
            └── __init__.py
            └── menu.py

```

## ▶️ Como rodar a aplicação

1. Clone o repositório ou baixe o código.
2. No terminal, acesse a pasta do projeto:

   ```bash
   cd src/

   python -m app.main
  
   ```

## 🧠 Para que serve?

- Esse projeto é perfeito para:

- Quem está dando os primeiros passos em Python.

- Quem quer entender como funciona o controle de fluxo (if, while, try/except).

- Quem curte projetos pequenos, mas com propósito.

### 💻 Feito com uma pitada de nostalgia por quem acredita que o básico bem-feito ainda é rei.
