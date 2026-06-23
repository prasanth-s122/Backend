# # Using Recursion

# a = int(input("Enter the number\n"))

# def sum(a):
#     if a == 1:
#         return 1
#     else:
#         return a + sum(a-1)
     
# print(f"Sum of {a} natural numbers is ----> {sum(a)}")

# # Factorial using recursion

# b = int(input("Enter the number to find factorial\n"))

# def fact(b):
#     if b==1:
#         return 1
#     else:
#         return b*fact(b-1)

# print(f"The factorial of {b} is ----> {fact(b)}")

# Task

c = int(input("Enter the number\n"))

def digit_sum(c):
    if c == 0:
        return 0
    else:
        x = c//10
        y = c % 10

        return y + digit_sum(x)
    
def digit_difference(c):
    if c == 0:
        return 0
    else:
        x = c//10
        y = c % 10

        return y - digit_difference(x)    

    
print(f"The sum of digits of {c} ----> {digit_sum(c)}")
print(f"The difference of digits of {c} ----> {digit_difference(c)}")
    
