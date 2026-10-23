#Implement a function to find the greatest common divisor (GCD) using recursion with Euclidean algorithm.
#Example: GCD(48, 18) -> 48 % 18 = 12, GCD(18, 12) -> 18 % 12 = 6, GCD(12, 6) -> 12 % 6 = 0 -> 6

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is: {gcd_recursive(num1, num2)}")