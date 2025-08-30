import datetime
currenttime = datetime.datetime.now()
print("Year:", currenttime.year)
print("Month:", currenttime.month)
print("Day:", currenttime.day)
print("Hour", currenttime.hour)
print("minute:", currenttime.minute)
print("second:", currenttime.second)

current_time = currenttime.strftime("%d/%m/%Y,%H:%M:%S seconds")
print("current time is", current_time)

name = input("Enter your name")
registration = input("Enter your registration numbera")
NEETSCORE = int(input("enter your 2025 NEET score:"))
if NEETSCORE >=700:
    print(f"Student {name} has been accepted into the university!!")
elif NEETSCORE >=660:
    print(f"Student {name} has been waitlisted")
else:
    print(f"Student {name} has rejected")