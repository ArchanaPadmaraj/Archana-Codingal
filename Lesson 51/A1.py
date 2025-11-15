# use while when you dont know how many loop (in number) you have to run use for i in range when you do know

# efficient method 01 
from math import sqrt
n = int(input("enter your number"))
for i in range (2,int(sqrt(n))+1):
    if n % i == 0:
        print("not a prime number")
        break
else:
        print("your number is prime")
    

# method 02 - generic

n2 = int(input("enter your number"))
count = 0 
for i in range (1,n2+1):
    if n2%i==0:
        count = count + 1
    
if count == 2:
    print("It is a prime number")
else:
     print("not a prime number")
