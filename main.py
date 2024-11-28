from classes import BankAccount, Bank

def main():
    client = BankAccount(1, "John", 1.0)
    bank = Bank()

    client.add_to_balance(5.0)
    client.show_account()
    client.substract_from_balance(3.0)
    client.show_account()

    bank.add_account(client)
    bank.show_accounts()

main()

