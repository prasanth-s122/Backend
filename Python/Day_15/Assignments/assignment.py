from sympy import symbols,expand

x = symbols("x")
y = symbols("y")
z = symbols("z")

# (x+y+z)^2
print("\n(x+y+z)^2\n")
print(list(map(lambda i : expand((x+y+z)**i),range(2,3))))

# (x-y)^2
print("\n(x-y)^2\n")
print(list(map(lambda i : expand((x-y)**i),range(2,3))))

# (x+y+z)^3
print("\n(x+y)^3\n")
print(list(map(lambda i : expand((x+y)**i),range(3,4))))