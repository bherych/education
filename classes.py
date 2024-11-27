class BankAccount:
    def __init__(self, id=0, owner_name="Unknown", balance=0.0):
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
    
class Bank:
    pass