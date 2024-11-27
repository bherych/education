from classes import BankAccount, Bank

def main():
    client = BankAccount(1, "John", 1.0)

    client.add_to_balance(5.0)
    client.show_account()
    client.substract_from_balance(3.0)
    client.show_account()

main()

