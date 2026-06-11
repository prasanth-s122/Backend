s1 = input("Enter subject 1\n").lower()
s2 = input("Enter subject 2\n").lower()
s3 = input("Enter subject 3\n").lower()

mark = int(input("Enter mark\n"))

if ((s1 != s2) and (s2 != s3) and (s3 != s1)) and s1 in ("chemistry","physics","maths") and s2 in ("chemistry","physics","maths") and s3 in ("chemistry","physics","maths") and mark >= 95 :
    print("Doctor")
elif ((s1 != s2) and (s2 != s3) and (s3 != s1)) and s1 in ("chemistry","physics","maths") and s2 in ("chemistry","physics","maths") and s3 in ("chemistry","physics","maths") and mark >= 85 :
    print("Engineering group")
elif ((s1 != s2) and (s2 != s3) and (s3 != s1)) and s1 in ("chemistry","physics","maths") and s2 in ("chemistry","physics","maths") and s3 in ("chemistry","physics","maths") and mark >= 75 :
    print("Arts and science")
else :
    print("Other group")    