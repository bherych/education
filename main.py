from classes import BankAccount, Bank

def main():
    client1 = BankAccount(1, "John", 1.0)
    client2 = BankAccount(2, "Steve", 55500.0)
    client3 = BankAccount(3, "Tom", 2300.0)
    bank = Bank()

    bank.add_account(client1)
    bank.add_account(client2)
    bank.add_account(client3)

    bank.show_accounts()
    bank.sort_accounts_by_balance()
    bank.show_accounts()

main()

