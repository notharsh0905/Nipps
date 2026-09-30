#Calculate Greatest Common Divisor (GCD) using recursion with Euclidean algorithm.
#Example: GCD(48, 18) -> 48 % 18 = 12, GCD(18, 12) -> 18 % 12 = 6, GCD(12, 6) -> 12 % 6 = 0 -> 6

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")