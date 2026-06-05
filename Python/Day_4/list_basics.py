
list = ["Prasanth",26,96.75,"Loki"]

list_2 = ["Witcher","Wild Hunt"]

print("The list is ",list)

print(list[0],list[3])

list.append(1000)

print(list)

list.extend(list_2)

print(list)

list_3 = list.copy()
print("Copied list is ",list_3)

print(list_3.pop())


print(list_3)

list_4 = [10,1,2,6,100,1000,99]

print(list_4)

list_4.sort()
print(list_4)

list_5 = ["B","A","a","L","l","b"]
print(list_5)

list_5.sort(key=str.upper)
print(list_5)


print("B" in list_5)

list.reverse()

print(list)


