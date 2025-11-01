def createlist (n):
    numbers = []
    count = 1
    for i in range(n):
        numbers.append(i)
        print(f"numbers of iteration is {count} and array of numbers is {numbers}")
        count +=1
    print(numbers)

createlist(8)