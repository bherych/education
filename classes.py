class BankAccount:
    def __init__(self, id, owner_name="Unknown", balance=0.0):
        self.__id = id
        self.__owner_name = owner_name
        self.__balance = balance

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    
    def get_owner_name(self):
        return self.__owner_name
    def set_owner_name(self, name):
        self.__owner_name = name

    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        self.__balance = balance

    def show_account(self):
        print(self.get_id(), self.get_owner_name(), self.get_balance())

    def add_to_balance(self, money):
        if isinstance(money, int):
            money_float = float(money)
            self.__balance += money_float
        else:
            self.__balance += money
            
        return print(f"Succesfully added {float(money)} to the balance")
    
    def substract_from_balance(self, money):
        if isinstance(money, int):
            money_float = float(money)
            self.__balance -= money_float
        else:
            self.__balance -= money

        return print(f"Succesfully substracted {float(money)} from the balance")
    
    def __str__(self):
        return (f"{self.get_id()}, {self.get_owner_name()}, {self.get_balance()}")
    
    def __del__(self):
        return print("Object deleted")
    
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: BankAccount):
        if any(acc.get_id() == account.get_id() for acc in self.accounts):
            print("Account with this ID already exists.")
        else:
            self.accounts.append(account)
            print(f"Account {account.get_id()} added.")
    
    def remove_account(self, id):
        for account in self.accounts:
            if account.get_id() == account.get_id():
                self.accounts.remove(account)
                print(f"Account {id} removed.")
                return
    
    def sort_accounts_by_balance(self):

        def get_balance(acc):
            return acc.get_balance()
        
        self.accounts.sort(key=get_balance)
        print("Accounts sorted by balance.")
    
    def sort_accounts_by_id(self):

        def get_id(acc):
            return acc.get_id()
        
        self.accounts.sort(key=get_id)
        print("Accounts sorted by id.")
    
    
    def show_accounts(self):
        for account in self.accounts:
            print(f"{account.get_id()}, {account.get_owner_name()}, {account.get_balance()}")

    def __str__(self):
        for acc in self.accounts:
            print(acc)
        return

    def __del__(self):
        return print("Bank destroyed")