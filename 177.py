#Implement a function to calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
#The GCD of two integers is the largest positive integer that divides both numbers without a remainder.
#Example: gcd(48, 18) = 6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")