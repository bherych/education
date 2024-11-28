from classes import BankAccount, Bank

def main():
    client = BankAccount(1, "John", 1.0)
    bank = Bank()

    client.add_to_balance(5.0)
    client.show_account()
    client.substract_from_balance(3.0)
    client.show_account()

    bank.add_account(client)
    i = 1
    for i in range(5):
        acc = BankAccount(i+1, "Unknown", (i*5.0)**5.0)
        bank.add_account(acc)
    bank.show_accounts()

main()

