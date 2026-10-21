#Implement a function to print the first n prime numbers.
#Example: n = 10 -> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

def print_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("Enter number of primes to generate: "))
primes = print_first_n_primes(n)
print(f"First {n} prime numbers: {primes}")