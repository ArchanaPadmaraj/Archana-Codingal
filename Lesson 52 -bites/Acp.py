number01 = 34
number02 = 6
print("number 01 & number2 are:", number01 & number02)
print("number 01 | number2 are:", number01 | number02)
print("number 01 ^ number2 are:", number01 ^ number02)
print("number 01 >> number2 are:", number01 >> number02)
print("number 01 << number2 are:", number01 << number02)
print("~ number 01 is ", ~number01)
print("~ number 02 is ", ~number02)

def evenorodd (n):
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
    
number = int(input("enter your number"))

if evenorodd (number):
    print(number,"is even")
else:
    print(number,"is odd")


def countofbits (n):
    count = 0
    while(n):
        count+=1
        n = n >> 1
    return count


n = int(input("please enter your number"))
print("the number of bits in your number are/is: ",countofbits(n))