#Given a 3-digit number, find the sum of its first and last digits.
#Example: 456 -> 4 + 6 = 10

num = int(input("Enter a 3-digit number: "))
first = num // 100
last = num % 10
print("Sum of first and last digits:", first + last)