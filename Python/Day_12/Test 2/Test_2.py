# Sum of numbers
print("Sum of 1 to 5")
sum = 0
i=1
while i<=5:
    sum = sum +i
    i=i+1
print(sum)

# space count in string
print("space count in string")
string_1 = input("Enter the string\n")
space_count = 0
for i in range(len(string_1)):
    if string_1[i] == " ":
        space_count = space_count+1

print("The number of spaces present is ---->",space_count)

# characters with index
print("characters with index")
string_2 = input("Enter the string\n")
for i in range(len(string_2)):
    print("Character -- ",string_2[i]," <----> ","Index -- ",i)

# Digit count in string
print("Digit count in string")
string_3 = input("Enter the string\n")
digit_count = 0
for i in range(len(string_3)):
    if(string_3[i].isdigit()):
        digit_count = digit_count+1
print("The digit count is ---->",digit_count)
# Reverse String using loops
print("Reverse string")
string_4 = input("Enter the string\n")
i = len(string_4)-1
reverse = ""

while i >=0:
    reverse+=string_4[i]
    i=i-1
print("Reversed string is ---->",reverse)


# Largest number in a list 
print("Largest number in a list")
list_1 =  [3, 7, 2, 9, 5]
print(list_1)
large = 0

for i in range(len(list_1)):
    if large < list_1[i]:
        large = list_1[i]

print("The largest element is ---->",large)

# count words
print("Word count")
word_count = 0
sentence = "i love python program"
print("The sentence is ---->",sentence)

for i in range(len(sentence)):
    if sentence[i]==" ":
        word_count = word_count+1

print("The number of words present is ---->",word_count+1)

# Common elements in list
print("Common elements in list")
a = [1, 2, 3, 4]

b = [3, 4, 5]

print("The lists are ----> ",a,b,sep="\n")
print("The common elements are ---->")

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            print(a[i])