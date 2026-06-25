list_1 = map(int,input("Enter the list\n").split())
list_2 = map(int,input("Enter the list\n").split())
print(list(map(lambda x,y:x+y,list_1,list_2)))

print(list(map(lambda a,b : 4*a*b+4*(a**2)*(b**2)+300,list_1,list_2)))


