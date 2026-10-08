#Implement a function to check if a number is a power of 2.
#A number is a power of 2 if it can be expressed as 2^n for some non-negative integer n.
#Example: 1 -> True (2^0), 8 -> True (2^3), 10 -> False

import math
num = int(input("Enter a positive integer: "))
if num > 0:
    is_power_of_2 = (num & (num - 1)) == 0
    print(f"{num} is a power of 2: {is_power_of_2}")
else:
    print(f"{num} is not a power of 2")