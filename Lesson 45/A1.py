def fun1(n):
    for i in range (1,11):
        print("constant")
    return n*(n+1)/2

def fun2(n):
    sum = 0
    for i in range(1,n+1):
        sum+=1
    return sum

def fun3(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            sum+=i*j
    return sum

print(fun1(4))
print(fun2(10))
print(fun3(12))