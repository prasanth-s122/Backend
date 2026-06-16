vehicle = input("Enter the Vehicle types ('comma seperator')\n").split(',')
fuel = input("Enter the Fuel type ('comma seperator')\n").split(',')

for i in range(0,len(vehicle)):

	for j in range(0,len(fuel)):
		
		print("Vehicle ---> ",i,"||","Fuel ----> ",j)
	
	print("\n")

