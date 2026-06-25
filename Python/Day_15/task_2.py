from sympy import symbols,expand
# 2 variables
a = symbols("a")
b = symbols("b")

print(list(map(lambda i:expand((a+b)**i),range(2,4))))
print("\n")

# 3 variables
c = symbols("c")
print(list(map(lambda i:expand((a+b+c)**i),range(2,4))))