a = int(input("Enter the starting table \n"))
b = int(input("Enter the ending table \n"))

c = int(input("Enter the starting number \n"))
d = int(input("Enter the ending number \n"))

print("The values are ---->")

for i in range(a,b+1):

	for j in range(c,d+1):

		print(j," * ",i," = ",i*j)
	
	print("\n-----------------------------\n")