friends = ["ashika","pooja","riya","lena"]

print("friends list:", friends)
print("first friend:",friends[1])
print("coolest friend:",friends[2])
print("newest friend:",friends[3])
print("smartest friend:",friends[0])

friends[2] = "akhina"
print("updated list of friends:",friends)

friends.append("archana")
print("updated list of friends:",friends)

friends.remove("pooja")
print('updated list of friends after few revisions:',friends)

count = 1
for i in friends:
    print(f"friend number {count} is - ", [i])
    count +=1