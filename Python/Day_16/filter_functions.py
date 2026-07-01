list_1 = list(range(0,25))

print("The list is ---->",list_1,"\n")

print(f"Even numbers are ----> {list(filter(lambda x:x%2==0,list_1))}\n")

# def function

def odd(n):
    if n%2!=0:
        return True
    else:
        return False

print(f"Odd numbers are ----> {list(filter(lambda x:odd(x),list_1))}\n")


age_list =list( map(int,input("Enter the values 'Space seperator' ----> ").split()))

print("The ages are ----> ",age_list)

print(f"The age above 18 are ----> {list(filter(lambda x:x>=18,age_list))}\n")