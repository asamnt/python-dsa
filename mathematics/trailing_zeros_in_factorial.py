n = int(input("Enter x:\n"))

# naive solution
factorial = 1
for i in range(2, n+1):
    factorial = factorial * i
result = 0
while(factorial % 10 == 0): # get the last digit and check if it is zero. if it is not zero, we exit the loop
    result = result + 1
    factorial = factorial // 10 #drop the last digit
print(result)


#efficient solution

result = 0
i = 5
#count the number of 5s
#count the number of 25s => 5 * 5
#count the number of 125s => 5 * 5 * 5
while (i <= n):
    result = result + (n // i)
    i = i * 5
print(result)
#time complexity log n
