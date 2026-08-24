#Given two numbers, find their Least Common Multiple (LCM).
#LCM(a, b) = (a * b) / GCD(a, b)
#Example: LCM(4, 6) = 12

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
import math
lcm = abs(a * b) // math.gcd(a, b)
print("LCM:", lcm)