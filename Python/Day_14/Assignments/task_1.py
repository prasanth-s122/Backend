# task 1

def mul():
    return 1, 2 ,3 

print(mul())

# task 2 calculator
a = int(input("Enter the first number\n"))
b = int(input("Enter the second number\n"))

def calculator(a,b):
    print("Addition---->",a+b)
    print("Subtraction---->",a-b)
    print("Multiplication---->",a*b)
    print("Division---->",a/b)

calculator(a,b)

# Prime number

x = int(input("Enter the number to check prime\n"))

def prime(x):
    if x < 2:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True

if prime(x):
    print(f"{x} is a prime number")

else:
    print(f"{x} is a not a prime number")

# Lambda
even = int(input("Enter the number to check even or not\n"))
check = lambda even : even % 2 == 0
if check(even):
    print("Even number")
else:
    print("Odd number")