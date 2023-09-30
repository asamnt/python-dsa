a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))

while a != b:
    if a > b:
        a = a-b
    else:
        b = b- a
print(a)