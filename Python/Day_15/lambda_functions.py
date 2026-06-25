import math as m
# fun = lambda x : x**2
# x = int(input("Enter the number\n"))
# print(f"Square of {x} is {fun(x)}")

# # Equations

# eqn = lambda a,b : a**2 + 2*a*b + b**2
# a = int(input("Enter the number\n"))
# b = int(input("Enter the number\n"))

# print(f"({a}+{b})^2 = {eqn(a,b)}")

# Square root of list 

list_1 = [1,4,9,16,25,36,49,64,81,100]
print(list_1)
square_root = lambda x : m.sqrt(x)

for i in list_1:
    print(f"Square root of {i} ----> {square_root(i)}")
print("\n")
# Cube of list
list_2 = [1,2,3,4,5,6,7,8,9,10]
print(list_2)

cube = lambda x : m.pow(x,3)
cube_list = []
for i in list_2:
    cube_list.append(cube(i))

print(f"\nCube of {list_2} is ----> {cube_list}")