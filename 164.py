#Implement a function to check if a number is a power of three.
#A number is a power of three if it can be expressed as 3^n for some non-negative integer n.
#Use the property that if n is a power of 3, then log_10(n) / log_10(3) is an integer.
#Example: 27 -> True (3^3), 0 -> False, 45 -> False

def is_power_of_three(n):
    if n <= 0:
        return False
    # The largest power of 3 within 32-bit integer range is 3^19 = 1162261467
    # If n is a power of 3, 1162261467 % n == 0
    return 1162261467 % n == 0

num = int(input("Enter a positive integer: "))
print(f"{num} is a power of three: {is_power_of_three(num)}")