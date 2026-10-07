#Implement a function to find the largest prime factor of a given number.
#Example: 28 -> 7 (since 28 = 2^2 * 7), 13195 -> 29

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1
    return n

num = int(input("Enter a number: "))
print(f"Largest prime factor of {num}: {largest_prime_factor(num)}")