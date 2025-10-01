class Animal:
    def make_sound(self):
        return "some generic animal sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Barkbark"

class Cat(Animal):
    def make_sound(self):
        return "meowmeow"

dog = Dog()
cat = Cat()
print(cat.make_sound())
print(dog.make_sound())


class Car:
    def start_engine(self):
        return "some random car has been started"

class BMW(Car):
    def start_engine(self):
        return "The BMW has started, please buckle your seatbelts"

class Audi(Car):
    def start_engine(self):
        return "The Audi has started, please buckle your seatbelts"
    
bmw = BMW()
audi = Audi()
print(bmw.start_engine())
print(audi.start_engine())
