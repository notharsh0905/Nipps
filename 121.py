#Check if a number is prime using trial division.
#A prime number is greater than 1 and has no divisors other than 1 and itself.
#Example: 7 -> True, 10 -> False

import math
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    print(f"{num} is prime: {is_prime}")
else:
    print(f"{num} is not prime")