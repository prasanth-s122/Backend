import functools as f

list_1 =list( map(int,input("Enter the values 'Space seperator' ----> ").split()) )

print(f"The list ----> {list_1}\n")

def large(a,b):
    if a>=b:
        return a
    else:
        return b

print(f"The largest number is ----> {f.reduce(large,list_1)}\n")

def small(a,b):
    if a<=b:
        return a
    else:
        return b

print(f"The smallest number is ----> {f.reduce(small,list_1)}\n")