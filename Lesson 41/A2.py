from abc import ABC, abstractmethod

class Vehicle (ABC):
    @abstractmethod
    def start_engine(self):
        pass
# pass = abstract method to be implemented in child class 
class Car(Vehicle):
    def start_engine (self):
        print("car engine started - vroom vroom")

    def stop_engine (self):
        print("car engine has stopped")
    
class Bike(Vehicle):
    def start_engine(self):
        print("the bike engine has started")
    def stop_engine (self):
        print("the bike engine has stopped")

obj1 = Car()
obj1.start_engine()
obj1.stop_engine()
obj2= Bike()
obj2.start_engine()
obj2.stop_engine()


from abc import ABC , abstractmethod

class Animal (ABC):
    @abstractmethod
    def sound (self):
        pass

class Dog(Animal):
    def __init__ (self,name):
        self.name = name
    def sound (self):
        print(f"{self.name} is barking")
    def walk(self):
        print(f"{self.name} is walking")

class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def sound (self):
        print(f"{self.name} is barking")
    def walk(self):
        print(f"{self.name} is walking")

cat1 = Cat("lucy")
cat1.sound()
cat1.walk()
dog1 = Dog("Vicky")
dog1.walk()
dog1.sound()