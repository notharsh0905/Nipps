#Calculate the power of a number using recursion.
#base^exponent where exponent is a non-negative integer.
#Example: 2^5 = 32

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(f"{base}^{exp} = {power(base, exp)}")