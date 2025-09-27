class Animal:
    def __init__ (self,name):
        self.name = name
    
    def eat (self):
        print(f"{self.name} is currently eating")
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def bark (self):
        print(f"{self.name}, the {self.breed} is barking")
    
dog1 = Dog("buddy","Husky")
dog1.eat() 
# parent class method
dog1.bark()
# child class method

# assignment

class Car:
    def __init__ (self,name):
        self.name = name
    def start (self):
        print(f"{self.name} is accelerating!")

class BMW(Car):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    def stop (self):
        print(f"The {self.name} car in {self.color} is coming to a stop")

car1 = BMW("BMW X5","Black Sapphire")
car1.start()
car1.stop()