n = int(input("Enter n:\n"))

#naive approach
def check_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_prime_eff(n):
    if n== 1:
        return False
    i = 2
    while ( i * i <= n):
        if n % i == 0:
            return False
        i +=1
    return True

is_prime = check_prime(n)
print(is_prime)
is_prime = check_prime_eff(n)
print(is_prime)

#efficient approach
# traverse till square root of n
# use while loop

