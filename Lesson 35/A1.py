def greet(name):
    print("hello",name)

response = input("enter your name")
greet(response)

def numbers(a,b):
    result = a+b
    print(f"the sum of {a} and {b} is {result}")

x = int(input("enter your first number"))
y = int(input("enter your second number"))
numbers(x,y)

def Guess():
    while True:
        guess = int(input("Enter a number from 1 to 10"))
        if guess == 5:
            print("You have guessed the number!!!")
        else:
            print("wrong! try again ")

Guess()