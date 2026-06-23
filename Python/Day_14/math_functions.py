import math as m
x = int(input("Enter the 1st input ----> \n"))
y = int(input("Enter 2nd input ----> \n")) 
print("The numbers are ----> ",x,y,sep="\n")
print("Absolute function",m.fabs(x))
print("Copy sign function ----> ",m.copysign(x,y))
e = int(input("Enter the power of e\n"))
print(f" e power {e} is ----> {m.exp(e)}")

# Log function 
l = int(input("Enter the number to find log base 2\n"))
print(f"Log base 2 of {l}----> {m.log2(l)}")

# Math functions on lists


# close functions 
a = int(input("Enter the 1st number ----> \n"))
b = int(input("Enter the 2nd input ----> \n"))

t = int(input("Enter the tolerance ----> \n"))

print(f"Is {a} close to {b} with tolerance {t} ?-----> {m.isclose(a,b,abs_tol = t)}")
