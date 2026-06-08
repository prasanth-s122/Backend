tuple_1 = (1,2,3,4,5,5,5,5,2,1,1,3,4,7)
print("Tuple 1 ---->",tuple_1,"\n","Type ---->",type(tuple_1))

print("Value of index 2 ---->",tuple_1[2])

# Packed things [*variable gives unallocated values as list]

(x,y,z)=(1,2,3)
print("x ---->",x)
print("x ---->",y)
print("x ---->",z)

(a,b,*c)=(10,20,30,40,50,60)
print("a ---->",a)
print("b ---->",b)
print("c ---->",c)

# count
print("Count of 1 in ",tuple_1, "---->",tuple_1.count(1))