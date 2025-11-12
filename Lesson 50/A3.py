a = int(input("enter your first number"))
b = int(input("enter your second number"))

if a>b:
    greater = a
else:
    greater = b

while True:
    if(greater % a == 0 ) and (greater % b == 0):
        print("lcm is ",greater)
        break
    greater+=1
    