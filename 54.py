def factorial(n):
    # Base case: 0! and 1! are 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n * (n-1)!
    return n * factorial(n - 1)

try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        raise ValueError("Number must be non-negative")
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError as e:
    print(f"Invalid input: {e}")   