#Given a positive integer, reverse its digits.
#Example: 1234 -> 4321

num = int(input("Enter a positive integer: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)