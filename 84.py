#Given two numbers, find their Greatest Common Divisor (GCD) using the Euclidean algorithm.
#Example: GCD(48, 18) = 6

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b
print("GCD:", a)