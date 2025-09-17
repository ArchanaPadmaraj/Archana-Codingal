people = ("archana","pooja","chandini","padmaraj","sunitha")
print("oldest member of the family:", people[-2])
print("cutest member of the family:", people[1])
print("youngest member of the family:", people[0])
print("smartest member of the family:", people[2])
print("most reliable member of the family:", people[4])

fam = {"archana","pooja","chandini","padmaraj","sunitha"}
fam.remove("chandini")
print("family members i currently live with:",fam)

count = 1
for i in people:
    print(f"the order of the people i love most is {count}.",i)
    count +=1

