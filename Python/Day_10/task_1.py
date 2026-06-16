list = input("Enter the list ('cs')").split(',')

print("The list is ---->",list)

print("First half values are")

for i in range(0,len(list)//2):
	print(list[i])

print("Second half values are ")

for i in range(len(list)//2,len(list)):
	print(list[i])