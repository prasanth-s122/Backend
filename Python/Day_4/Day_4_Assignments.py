# First task

str1 = "python"
print("Upper case is ",str1.upper())
print("Lower case is ",str1.lower())
print("Capitalize  ",str1.capitalize())
print("Count of p is ",str1.count("p"))
print("Index of p is ",str1.index("p"))

# Second task
sentence = "java is easy to learn"
print("The sentence ---->",sentence)
sentence = sentence.replace("java","python")
print("Replaced sentence ---->",sentence)
s1 = sentence.split()
print("Splitted sentence ---->", s1 , "\n" "Type ---->",type(s1))
s2 = " ".join(s1)
print("Joined string ---->",s2, "\n" "Type ---->",type(s2))

# List tasks
name = ["Abi","Akash","Alex"]
print("List ---->",name)
print("First element ---->",name[0])
print("Sliced name ---->",name[1:2])
name.append("Priya")
print("List after appending a name ---->", name)
name.extend(["Ajay","Ajith"])
print("List after extend ---->",name)
name.insert(1,"Jack")
print("List after insertion ---->",name)

# Sorting and reversing

num = [10,7,2,1,18]
num.sort()
print("Sorted list ---->",num)

num.reverse()
print("Reversed list ---->",num)