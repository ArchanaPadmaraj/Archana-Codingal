class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
        print(f"Hello user named {self.name} whose age is {self.age}")
    
    def greet (self):
        print(f"Welcome {self.name} to Codingal")

    def __del__ (self):
        print(f"User {self.name}'s data has been erased successfully")

print("Creating....Please Wait!.....")
user1 = Person("Achu","15")
user1.greet()

print("Do you wish to delete data?")
answer = input()
if answer == "yes":
    del user1

ageqs = int(input("how old are you?"))
if ageqs >=18:
    print("Enjoy the game")
else:
    print("You are not old enough to play the game!")