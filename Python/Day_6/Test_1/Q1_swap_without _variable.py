a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))
print("The numbers are ",a,b)
a = a + b
b = a - b
a = a - b

print("The numbers after swap are ",a,b,sep='\n')