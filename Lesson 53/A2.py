def setornot (number,n):
    if number & (1 << (n - 1)):
        print("SET")
    else:
        print("NOT A SET")

number = int(input("enter your number"))
n= int(input("enter the bit position"))
setornot(number, n)