class Animal:
    def __init__(self,name):
        self.name = name
        print(f"{self.name}'s object has been created")

    def sound (self):
        print(f"{self.name} is now making sound")
    
    def walk(self):
        print(f"{self.name} is now walking")
    
    def __del__ (self):
        print(f"{self.name} has been deleted")
    
dog = Animal("Vicky")
dog.sound()
dog.walk()

cat = Animal("Lucy")
cat.walk()
cat.sound()

del dog
del cat
# cat.sound () or dog.sound() will not work since the object has been deleted. therfore will show you error
