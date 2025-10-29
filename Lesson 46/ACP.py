def project (n):
    iteration = 0
    for i in range(0,n+1):
        for j in range(0,n+1):
            print("*",end=" ")
            iteration +=1
        print(" ")
    print ("when n is",n,"iteration is",iteration)

project(5)
project(4)
project(8)