friend01 = {
    "name":"Jovita",
    "age":14,
    "class":"10C",
    "DOB": "22nd Septemeber 2010"
}

friend02 = {
    "name":"Akhina",
    "age":15,
    "class":"10C",
    "DOB": "5th March 2010"
}

friend03 = {
    "name":"Pooja",
    "age":15,
    "class":"10C",
    "DOB": "4th August 2010"
}

friends = [friend01 , friend02 , friend03]

print(friends)

count = 1
for i in friends:
    print(f" information on friend {count} is - ",[i])
    count +=1