#Implement a function to calculate the least common multiple (LCM) of two numbers.
#The LCM of two integers is the smallest positive integer that is divisible by both numbers.
#LCM(a, b) = (a * b) / GCD(a, b)
#Example: lcm(4, 6) = 12

def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")