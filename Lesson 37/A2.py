student_info = {
    "name" :"archana",
    "age" : 15,
    "grade" : "10th",
}

print("dictionary:",student_info)
print("Name of student:",student_info["name"])

student_info["school"] = "XYZ HIGH SCHOOL"
print("updated dictionary:",student_info)

student_info["name"] = "Archana Padmaraj"
print("edited dictionary:",student_info)

del student_info["age"]
print("student info:",student_info)

print("iterating throught the information -")
for key, value in student_info.items():
    print(key, ":", value)
