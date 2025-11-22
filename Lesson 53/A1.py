def numberofbites(n):
    zeroes = 0
    ones = 0
    while(n):
        if(n & 1 == 1):
            ones +=1
        else:
            zeroes+=1
        n = n >> 1
    print("number of ones = ",ones,"number of zeroes = ",zeroes)

number = int(input("enter your number"))
numberofbites(number)