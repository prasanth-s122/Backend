country = input("Enter the country\n").lower()
age = int(input("Enter the age\n"))

if age >= 18:
	if country == "india":
		print("Eligible to vote in india")
	else:
		print("Not eligible to vote in india")
else:
	print("Not eligible to vote")

