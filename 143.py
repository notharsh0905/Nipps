#Implement a function to find the factorial of a number using recursion with memoization.
#Cache previously computed factorials to improve performance for repeated calls.

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_memo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_memo(n - 1)

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"{num}! = {factorial_memo(num)}")