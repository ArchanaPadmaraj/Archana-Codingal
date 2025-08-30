# # # voting system
print("Welcome to the voting system")
name = input("Whats your name?")
age = int(input("How old are you?"))
if age >=18 :
    print(f"{name} is eligible to vote")
else:
    print(f"{name} is not old enough to vote")

# # # odd or even
print("Welcome to the even or odd calculator!")
number = int(input("please enter your number!"))
if number%2==0:
    print(f"{number} is a even number")
else:
    print(f"{number} is an odd number") 

# # multiple if and else
num = int(input("enter your number"))
if num > 0:
    if num%2==0:
        print(f"{num} is a positive even number")
    else:
        print(f"{num} is a positive odd number")
else: 
    print(f"{num} is a negative number")

# if-elif-else statements
name1= input("enter your name")
marks = int(input("Please enter your marks"))
if marks>=90:
    print(f"{name1} has passed and your grade is A")
elif marks>=75:
    print(f"{name1} has passed and your grade is B")
elif marks>=65:
    print(f"{name1} has passed and your grade is C")
elif marks>=50:
    print(f"{name1} has passed and your grade is D")
else:
    print(f"{name1} has failed")






# new code

import datetime

# Current date and time

# module.class.method()

currentTime = datetime.datetime.now()

print("Current Date and Time:", currentTime)

# Extracting date and time

print("Year:", currentTime.year)

print("Month:", currentTime.month)

print("Day:", currentTime.day)

print("Hour:", currentTime.hour)

print("Minute:", currentTime.minute)

print("Second:", currentTime.second)

# Formatting date and time

formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%S")

print("Formatted Date and Time:", formatted_time)