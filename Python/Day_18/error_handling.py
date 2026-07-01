try:
    a = int(input("Enter the First number\n"))
    b = int(input("Enter the Second number\n"))

    c = a/b
    print(c)

except ZeroDivisionError:
    print("Second number cannot be 0 ❌\n")

except ValueError:
    print("Do not enter alphabets and special characters ❌\n")

finally:
    print("<---- Program executed successfully 😊 ---->\n")

