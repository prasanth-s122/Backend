# for loop

list = ["python","java","C","C++"]

print("List is ",list)

print("For loop output")
for i in list:
	print(i)


print("Single sentence is ")

for i in list:
	print(i,end=' ')

print("Range function -----> Numbers from 0 to 9----->")

for i in range(0,10):
	print(i)


print("Range function -----> Odd Numbers from 0 to 9----->")

for i in range(1,10,2):
	print(i)

print("Range function -----> Even Numbers from 0 to 9----->")

for i in range(0,10,2):
	print(i)