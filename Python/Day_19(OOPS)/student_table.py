class student_table:
    def __init__(self,student_id,student_roll,student_name,student_gender,student_course):
        self.__student_id = student_id
        self.__student_roll = student_roll
        self.student_name = student_name
        self.student_gender = student_gender
        self.student_course = student_course
    
    def table(self):
        print(self.student_name,self.__student_id,self.__student_roll,self.student_name,self.student_gender,self.student_course,sep='\n')
    

id = int(input("Enter the Student ID\n"))
roll = int(input("Enter the Student Roll Number\n"))
name = input("Enter student name\n")
gender = input("Enter student gender\n")
course = input("Enter student course\n")

student_1 = student_table(id,roll,name,gender,course)
print("<---- The details are ---->")
student_1.__student_id = 22
student_1.__student_roll = 2000
student_1.table()