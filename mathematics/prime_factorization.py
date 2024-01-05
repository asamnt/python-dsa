n = int(input("Enter n:\n"))


def check_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    for i in range(2, n+1):
        if check_prime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i
prime_factors(n)