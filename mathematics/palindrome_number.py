n = int(input("Enter x:\n"))
reverse = 0
temp = n
while temp != 0:
    # with modulo operation we get the last digit
    last_digit = temp % 10
    # as we are shifting the digit to the left, we multiply by 10
    reverse = reverse * 10 + last_digit
    # to get the remaining digits, we do a floor operation
    temp = temp // 10
print(reverse == n)
