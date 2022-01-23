# A class is like a blueprint for creating objects. an object has properties
# and methods(functions) associated with it. Almost everything in Python is an object


# Create a Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} years old"

    def has_birthday(self):
        self.age += 1


# Extend a class
class Customer(User):
    # Constructor
    # def __init__(self, name, email, age):
    #     self.name = name
    #     self.email = email
    #     self.age = age
    #     self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} years old and my balance is {self.balance}"


# initialize user object
mutua = User("Joseph Mutua", "mutua@gmail.com", 45)

# init Customer object
janet = Customer("Janet", "janet@gmail.com", 34)

janet.set_balance(5000)
print(janet.greeting())

print(type(mutua))
mutua.has_birthday()
print(mutua.greeting())