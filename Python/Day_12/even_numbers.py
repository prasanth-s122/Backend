i = 0
print("Even numbers Increasing order")
while i <= 50:
	if i%2==0:
		print(i)
	i=i+1

print("Even numbers Decreasing order")

j = 50

while j >= 0:
	if j%2==0:
		print(j)
	j=j-1


print("Numbers from 150 to 100 ---> Decrement by 3")

a = 150

while a >= 100:
	print(a)
	a = a-3



print("Numbers from 0 to 10 ---> Ignore 5,6,7")

b =0

while b <= 10:
	if b in (5,6,7):
		b = b+1
		continue
	print(b)
	b = b+1	 
	
	