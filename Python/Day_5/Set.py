set_1 = {"1","1","2","3","4","4","0"}
print("Set 1 ---->",set_1,"\n","Type ---->",type(set_1))

# Set functions

set_1.add("10")
print("Add function ---->",set_1)

set_2 ={"a","b","c","d"}
print("Set 2 ---->",set_2,"\n","Type ---->",type(set_2))
set_1.update(set_2)
print("Update function ---->",set_1)

set_1.remove("1")
print("Set 1 after remove() ---->",set_1)

set_2.discard("100")
print("Set 2 after discard() ---->",set_2)

set_2.clear()
print("set 2 after clear ---->",set_2)

set_3 = set_1.copy()
print("Set 3 after copy() ---->",set_3)

print("Popped element ---->",set_3.pop())
print("Set 3 after pop() ---->",set_3)

set_4 = {1,2,3,4,5,6,7,8,9}
set_5 = {2,4,6,8}
set_6 = {3,6,9,12,15,18}


print("Set 4 ---->",set_4)
print("Set 5 ---->",set_5)
print("Set 6 ---->",set_6)
print("union() ---->",set_4.union(set_5,set_6))

print("intersection() ---->",set_4.intersection(set_5,set_6))


print("Set 4 before intersection_update()  ---->",set_4)
set_4.intersection_update(set_5,set_6)
print("Set 4 after intersection_update() ---->",set_4)


# Difference function
set_7 = {1,2,3,4,5,6,7,8,9,10}
print("Set 7 ---->",set_7)
print("difference of set 7 and 5 ---->",set_7.difference(set_5))

print("Set 7 before difference_update()  ---->",set_7)
set_7.difference_update(set_5)
print("Set 7 after difference_update()  ---->",set_7)

# symmetric difference 

set_8 = {1,2,9,12,15,18,21,24,27,30}
print("Set 6 ---->",set_6)
print("Set 8 ---->",set_8)
print("symmetric difference of set 8 and 6 ---->",set_6.symmetric_difference(set_8))

print("Set 8 before symmetric difference_update()  ---->",set_8)
set_8.symmetric_difference_update(set_6)
print("Set 8 after symmetric difference_update()  ---->",set_8)


# Additional info

set_9 = {1,True,False}
print(set_9)




