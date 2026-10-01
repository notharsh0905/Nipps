#Find the factorial of a number using a while loop.
#Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"{num}! = {factorial}")