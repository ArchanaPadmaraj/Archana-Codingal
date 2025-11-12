number = int(input("enter the number you want factors for"))
print("the factors for",number,"are :")
for i in range(1,number+1):
    if number%i == 0:
        print(i,end=" ")