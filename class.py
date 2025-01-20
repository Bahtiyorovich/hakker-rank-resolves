# Encapsulation - tashqi muhitdan yashirish

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  #yashirin atributi

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Yaroqsiz miqdor!")

# account = BankAccount("Ali", 1000)
# print(account.get_balance())
# account.deposit(500)
# print(account.get_balance())


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def details(self):
        return f"{super().details()}, Doors: {self.doors}"

class Motorcycle(Vehicle):
    def details(self):
        return f"{super().details()}, Type: Motorcycle"

car = Car('BMW', "M5", 4)
bike = Motorcycle("Yamaxa", "R1")

vehicles = [car, bike]

# for vehicle in vehicles:
#     print(vehicle.details())


# @staticmethod: Real loyihadagi misol: Ma'lumotlarni formatlash
# Masalan, foydalanuvchi ma'lumotlarini qayta ishlovchi biror loyihada:

class UserUtils:
    @staticmethod
    def validate_email(email):
        """User emailini tekshiradi"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

# print(UserUtils.validate_email('test@gmail.com'))
# print(UserUtils.validate_email('exp-test@gmail-com'))

import json

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['name'], data['price'])

json_data = '{"name":"Python", "price":15000}'
product = Product.from_json(json_data)
# print(product.name)
# print(product.price)


class DiscountCalculator:
    @staticmethod
    def calculate_discount(price, discount):
        return price - (price * discount / 100)

# print(DiscountCalculator.calculate_discount(78000, 15))


class Player:
    level_up_threshold = 100

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def calculate_level(score):
        return score // Player.level_up_threshold


    @classmethod
    def update_threshold(cls, new_threshold):
        cls.level_up_threshold = new_threshold


# print(Player.calculate_level(250))
# Player.update_threshold(150)
# print(Player.calculate_level(250))


# Multiple Encapsulation

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Mammal created")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Bird created")

class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
        print("Bat created")

bat = Bat('Bruce')



















