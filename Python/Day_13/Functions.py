# first = int(input("Enter the first number\n"))
# second = int(input("Enter the second number\n"))
# third = int(input("Enter the third number\n"))

# def arithmetic_operations(a,b,c):
#     print("Addition is ----> ",a+b+c)
#     print("Subtraction is ----> ",a-b-c)
#     print("Multiplication is ----> ",a*b*c)
#     print("Division is ----> ",a/b/c)

# arithmetic_operations(first,second,third)

# Student details

student_name = input("Enter name \n")
student_age = int(input("Enter age\n"))
student_roll = int(input("Enter roll number\n"))

def details(name,age,roll):
    return (f"Name ----> {name},Age ----> {age},Roll number ----> {roll}")

details(student_name,student_age,student_roll)