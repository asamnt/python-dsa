n = int(input("Enter n:\n"))

def all_divisors(n):
    i = 1
    while ( i * i <= n):
        if (n % i == 0):
            print(i)
            if(i != n/i):
                print(n/i)
        i += 1

all_divisors(n)