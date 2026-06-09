tuple_1 = (1,2,3,4,5)
print("The tuple is ---->",tuple_1)

a = list(tuple_1)

a.append(100)

b = tuple(a)

print("Adding element ---->",b)

c = list(b)

c.remove(2)


d = tuple(c)

print("Remove ---->",d)


