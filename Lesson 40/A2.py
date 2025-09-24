class Student:
    def __init__ (self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"{self.name}'s record has been created")
    
    def showdetails (self):
        print(f"Name of student:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grade:{self.grade}")
    
    def updategrade (self,newgrade):
        self.grade = newgrade
        print(f"Student {self.name}'s grades has been updated to {self.grade}")

    def __del__ (self):
        print(f"Records of student {self.name} has been deleted")

Student01 = Student("Archana",15,"10th")
Student02 = Student("Pooja",14,"9th")
Student01.showdetails()
Student02.showdetails()
del Student02
del Student01
