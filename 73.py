#Given a base and exponent, compute base^exponent using a loop (no built-in power operator).
#Example: 2^5 = 32

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for _ in range(exp):
    result *= base
print(f"{base}^{exp} = {result}")