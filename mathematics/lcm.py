a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))
def lcm(a, b):
    result = max(a, b)
    while True:
        if result % a ==0 and result % b ==0:
            return  result
        result += 1
    return result
lcm = lcm(a, b)
print(lcm)

# efficient approach => a * b = gcd(a, b) * lcm (a, b)