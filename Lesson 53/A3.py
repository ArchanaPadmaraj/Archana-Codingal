def countbites (n):
    count = 0
    while(n):
        if n & 1:
            count +=1
        n >>= 1 
    return count

num = int(input("enter your number"))
ans = countbites(num)
print("number of set bites in", num, "is",ans)