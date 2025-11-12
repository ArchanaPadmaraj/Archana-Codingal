num_largest = int(input("enter the larger number of your choice"))
num_smallest = int(input("enter the smallest number of your choice"))

while num_smallest:
    num_store = num_smallest
    num_smallest = num_largest % num_smallest
    num_largest = num_store

print("HCF or GCD is ",num_largest)