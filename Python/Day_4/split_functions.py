sentence="hello , this @ is @ a code for split functions"

s1=sentence.split()

print("Sentence after default split",s1)

# print("Data type is ",(type(s1)))

s2=sentence.split('@')
print(s2)


s3=' '.join(s1)

print(s3)
