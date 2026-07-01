class student_studentlication:
    def __init__(self,name,age,education,address,gender):
        self.name=name
        self.age=age
        self.education=education
        self.address=address
        self.gender=gender
    
    def course(self):
        print("Courses available ----> Python Full Stack,Java Full Stack")


name = input("Enter name of the student\n")
age = int(input("Enter the age of the student\n"))
education = input("Enter education of the student\n")
address = input("Enter address of the student\n")
gender = input("Enter gender of the student\n")

student = student_studentlication(name,age,education,address,gender)

print(f"Name ----> {student.name}")
print(f"age ----> {student.age}")
print(f"Education ----> {student.education}")
print(f"Address ----> {student.address}")
print(f"Gender ----> {student.gender}")
print(f"Course is ----> ")
student.course()