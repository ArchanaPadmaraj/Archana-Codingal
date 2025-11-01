def binary_search (arr,target):
    left,right = 0 , len(arr) - 1
    iterations = 0

    while left <= right:
        iterations +=1
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"You have found the value of {target} in {iterations} iterations")
            return

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    print(f"you have found the value of {target} in {iterations} iterations")

numbers = [1,2,3,4,5,6,7,8,9,11,12,13,14,15]
binary_search(numbers,13)


# counter

def counter(n):
    if n == 0:
        print("done!")
        return
    print("the counter is at",n)
    counter(n-1)

counter(13)

# factorial

def Factorial (n):
    if n==1:
        return 1
    return n * Factorial(n-1)

print (Factorial(8))