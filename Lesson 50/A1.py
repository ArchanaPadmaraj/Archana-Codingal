num = int(input("please enter your number"))

og_num = num
reversed_num = 0

while num > 0:
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit
    num //= 10

if og_num == reversed_num:
    print(f"your entered number {og_num} is a palindrome")
else:
    print(f"your entered number {og_num} is not a palindrome, try again!")

# trick for comparison
# og_num = num
# reversed_num = num[::-1]