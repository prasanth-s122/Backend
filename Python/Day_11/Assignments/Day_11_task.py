no = [10,11,12,13]

print("The list is ---->",no)

sum = 0
for i in range(0,len(no)):
    sum += no[i]

print("Sum of the elements are --->",sum)

count = 0

for i in no:
    count += 1

print("No. of elements present is --->",count)

large = 0

for i in range(0,len(no)):

    if large < no[i]:
        large = no[i]

print("The largest number is ---->",large)