attendance = int(input("Enter attendance % \n"))
mock = int(input("Enter mock score % \n"))

if attendance >= 85:
	if mock >= 90:
		print("Placed")
	else:
		print("Not Placed")
else:
	print("Not eligible for placement")