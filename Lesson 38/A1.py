# touple - () , set - {}, list - []
# touple
friends = ("pooja","chandini","sarah","ashika")
print(friends)

print("the funniest friend:",friends[3])
print("the smartest friend:",friends[1])
print("the tallest friend:",friends[2])
print("the prettiest friend:",friends[0])
print("the my bestfriend:",friends[-2])

# slicing
print("slicing the touple:", friends[0:2])

count = 1
for i in friends:
    print(f"\n friend number {count} is:", i)
    count +=1 
# you can write count = count+1 too

# set arranges number in ascending order since they can understand numbers, but not alphabets
numbers = {1,2,3,4,5,6,7,3,1,0}
print(numbers)
numbers.add(11)
print(numbers)
numbers.remove(7)
print(numbers)

alphabets = {'a','r','c','h','a','n','a'}
print(alphabets)
alphabets.add('P')
print(alphabets)
alphabets.remove('a')
print(alphabets)


set01 = {1,3,5,7,9,0}
set02 = {2,4,6,8,0}

print("union of two sets are:", set01.union(set02))
print("intersection of two sets are:",set01.intersection(set02))
print(" elements from set 1 that are not in set 02 are:",set01.difference(set02))
print("elements from set 2 that are not in set 01 are:", set02.difference(set01))