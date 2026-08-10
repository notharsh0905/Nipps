#Given a positive integer, find the sum of its digits.
#Example: 1234 -> 1 + 2 + 3 + 4 = 10

num = int(input("Enter a positive integer: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)