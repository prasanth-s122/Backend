
subject = input("Enter the student's subject \n").lower()
course = input("Enter the student's course \n").lower()

if subject == "python":
	if course == "pfs":
		print("The student's course is Python Full Stack")
	elif course == "da":
		print("The student's course is Data Analyst")
	else:
		print("The student's course is other course")

else:
	print("The student's course is Other than Python course")

