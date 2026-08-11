# Classes, Objects, __init__, Inheritance, Polymorphism, Encapsulation, Abstraction

# Class: A blueprint that defines what data (variables/locators) and actions (functions/methods) a specific thing should have.
# Object: A physical instance built from that blueprint.

# Selenium Context: You will create a Class for every single web page 
# in your application (e.g., LoginPage, HomePage). 
# An Object is created when your test actually navigates to that page 
# and needs to interact with it.


class LoginPage:
    url = "https://example.com/login"

    def click_login_btn(self):
        print("clicking the login btn")

my_login = LoginPage()
my_login.click_login_btn()


#init 
# __init__ method is a special function that runs automatically 
# the exact moment an object is created.

# class Dog:

#     def bark(self):
#         print("Dog barks")

# my_dog = Dog()
# my_dog.name = "tommy"
# my_dog.bark()


# __init__ stands for initialize (which just means "set up").

# It acts like a bouncer at the door. Saying: "You can't create a Dog object 
# unless you give me a name for it right now."

class Dog:

    def __init__(self,dog_name):
        self.name=dog_name

    def bark(self):
        print(f"{self.name} is barking")

my_dog = Dog("tommy")
my_dog.bark()



#inheritance
class Cat:

    def __init__(self,cat_name):
        self.name = cat_name

    def meow(self):
        print(f"{self.name} is meowing")

class Kitty(Cat):

    def play(self):
        print(f"{self.name} is bitting ur shoes")


my_cat = Kitty("Chea")
my_cat.meow()
my_cat.play()


# "Poly" means many, and "morph" means forms.
# using the exact same method name for different objects, but each object does it in its own unique way.

class Cow:

    def speak(self):
        print("Moooo")

class Lion:

    def speak(self):
        print("Raaaaahh")


my_cow=Cow()
my_lion=Lion()
my_cow.speak()
my_lion.speak()


#encapsulation
# Encapsulation is like putting a protective shield around your data.
# It hides the internal details so outside code cannot accidentally mess 
# it up. In Python, we put two underscores __ in front of a variable name
# to make it "private".


class BankAccount:
    def __init__(self):
        # The double underscore makes the money private and protected
        self.__balance = 1000 

    def view_balance(self):
        print(f"Your balance is ${self.__balance}")

account = BankAccount()
account.view_balance()
# Output: Your balance is $1000

# If you try to print(account.__balance) down here, Python will crash! 
# It is locked inside the class.
# print(account.__balance)


# Abstraction
# Abstraction is like driving a car. You know that pressing the gas 
# pedal makes the car move forward. 
# You don't need to know how the engine mixes fuel and air.

from abc import ABC, abstractmethod

class Vechile(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vechile):

    def move(self):
        return "Car is moving"

my_car=Car()
print(my_car.move())



