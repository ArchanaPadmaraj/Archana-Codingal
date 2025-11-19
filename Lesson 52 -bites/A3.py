def countofbits (n):
    count = 0
    while(n):
        count+=1
        n = n >> 1
    return count


n = int(input("please enter your number"))
print("the number of bits in your number are/is: ",countofbits(n))