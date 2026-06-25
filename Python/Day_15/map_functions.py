# Cube using map function
import math as m
list_1 = [1,2,3,4,5,6,7,8,9,10]
print(list_1)
print(f"Square of {list_1} ----> {list(map(lambda x : m.pow(x,2),list_1))}")
print(f"Cube of {list_1} ----> {list(map(lambda x : m.pow(x,3),list_1))}")

list_2 = input("Enter the values \n").split()
print(f"List is ---->{list_2}")

print(f"Converted list is ---->{list(map(int,list_2))}")