#Given a positive integer, find its factorial.
#Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

num = int(input("Enter a positive integer: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")