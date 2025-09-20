class Nike:
    def __init__ (self,color,type):
        self.color = color
        self.type = type

    def details(self):
        print(f"the nike product is a {self.type} in {self.color} color")
    
niketshirt = Nike("white","Tshirt")
niketshirt.details()

# activity 01

class Bottle:
    def __init__(self,drink,quantity):
        self.drink = drink
        self.quantity = quantity

    def details01 (self):
        print(f"this bottle contains {self.quantity}ml of {self.drink}")

bottlesoda = Bottle("250","Coco Cola")
bottlesoda.details01()

# activity 02

class Toyota:
    def __init__(self,model,color,engine):
        self.model = model
        self.color = color
        self.engine = engine
    def details02 (self):
        print(f"the model {self.model} of Toyota comes in the color {self.color} has a {self.engine} engine")
    
Car = Toyota("Toyota Corolla XLE","Black Sand Pearl","1.8 L inline‑4")
Car.details02()