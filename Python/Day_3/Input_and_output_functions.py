name=input("Enter the name : ")
age=int(input("Enter the age : "))
marks=float(input("Enter the mark : "))
print(name,age,marks,sep=' | ', end = ' !! ')
print('\n')
print("Multiple defined output")
print("Name is : ",name,"Age is : ",age,"Mark is : ",marks,sep='\n')
print('\n')

print("F string")

print(f'Name of the student is : {name} , Age of the student is : {age} , Mark of the student is : {marks}')