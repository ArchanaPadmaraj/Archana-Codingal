def firstset (n):
    count = 1
    while(n):
        if n & 1 == 1:
            print("the first set is at ",count,"position")
            break
        else:
            count = count + 1
        n = n >>1

num = int(input("enter your number"))
firstset(num)