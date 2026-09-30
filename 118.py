#Calculate factorial of a number using recursion.
#Base case: 0! = 1 and 1! = 1
#Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"{num}! = {factorial(num)}")