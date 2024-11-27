class Car:

    def __init__(self, brand="Unknown", engine_power=0, max_speed=0, name="Unknown", number=0):
        self.__brand = brand
        self.__engine_power = engine_power
        self.__max_speed = max_speed
        self.name = name
        self.number = number

    def get_engine_power(self):
        return self.__engine_power

    def set_engine_power(self, engine_power):
        self.__engine_power = engine_power

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_name(self):
        return self.name

    def set_name (self, name):
        self.name = name

    def get_number(self):
        return self.number
    
    def set_number(self, number):
        self.number = number

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

    def __del__(self):
        pass

def main():
    mercedes = Car("Mercedes", 300, 200, "M1", 1)
    print(f"Brand {mercedes.get_brand()}, engine power = {mercedes.get_engine_power()}, max speed = {mercedes.get_max_speed()}, name of the car {mercedes.get_name()}, number {mercedes.get_number()}")
    bmw = Car("BMW", 300, 200, "M1", 2)
    print(f"Brand {bmw.get_brand()}, engine power = {bmw.get_engine_power()}, max speed = {bmw.get_max_speed()}, name of the car {bmw.get_name()}, number {bmw.get_number()}")
    toyota = Car("Toyota", 300, 200, "M1", 3)
    print(f"Brand {toyota.get_brand()}, engine power = {toyota.get_engine_power()}, max speed = {toyota.get_max_speed()}, name of the car {toyota.get_name()}, number {toyota.get_number()}")

main()