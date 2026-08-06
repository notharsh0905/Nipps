import math

try:
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    if den == 0:
        print("Error: Denominator cannot be zero.")
    else:
        # Find the Greatest Common Divisor
        common = math.gcd(num, den)
        
        # Simplify the fraction
        simplified_num = num // common
        simplified_den = den // common
        
        print(f"Simplified fraction: {simplified_num}/{simplified_den}")

except ValueError:
    print("Error: Please enter valid integers.")   