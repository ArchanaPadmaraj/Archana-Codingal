# armstrong number is when a number is the sum of the digits raised to the power which is the number of digits
# to get the last digit of the armstrong number the modulus of the number with 10 will be the last digit
# using floor division you'll get the first 2 digits

number = int(input("enter your desired number"))
result = 0 
temp = number

while temp !=0:
    digit = temp%10
    result = result+digit**3
    temp = temp//10
print(result)

if number == result:
    print("The entered number is a amstrong number")
else:
    print("the entered number is not a armstrong number")

    