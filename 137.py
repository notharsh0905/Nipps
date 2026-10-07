#Implement a function to check if a number is a perfect square.
#Return True if the number is a perfect square, False otherwise.
#Example: 16 -> True, 20 -> False

import math
num = int(input("Enter a number: "))
if num < 0:
    print(f"{num} is not a perfect square")
else:
    root = int(math.sqrt(num))
    print(f"{num} is a perfect square: {root * root == num}")