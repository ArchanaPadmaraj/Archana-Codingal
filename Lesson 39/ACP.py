class Mobile:
    def __init__(self,model,color,data):
        self.model = model
        self.color = color
        self.data = data
    def details (self):
        print(f"The newest apple phone that is the {self.model} in now available in the color {self.color} and has storage options till {self.data}")

apple = Mobile("iPhone 15 Plus","Green","512 GB")
apple.details()