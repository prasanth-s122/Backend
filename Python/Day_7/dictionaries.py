dictionary = {"name" : "Prasanth" , "roll" : 1 , "subject" : "python"}

print(dictionary,type(dictionary), sep = '\n')

print("Keys are ---->",dictionary.keys())
print("Values are ---->",dictionary.values())
print("Items are ---->",dictionary.items())

d2 = {"city" : "Chennai" , "state" : "Tamil Nadu"}

dictionary.update(d2)

print("After update() ---->",dictionary)

d3 = dictionary.copy()

print("d3 is ---->",d3)

print("Pop() ---->",d3.pop("roll"))
print("d3 after pop() ---->",d3)

# d3.clear()
# print(d3)
print(d3.get('name'))

# key with multiple values

d4 = {"roll" : [1,2,3],"age" : [26,27,28],"name" : ["Prasanth","Loki","James"]}
print("Multiple values ---->",d4)
print(type(d4))

print(d4["name"][1])
