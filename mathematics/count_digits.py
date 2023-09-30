x = int(input("Enter x:\n"))

res = 0
while x > 0:
    x = x // 10
    res = res + 1
print(res)