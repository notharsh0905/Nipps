#Implement a function to find the cube sum of first n natural numbers.
#Formula: 1^3 + 2^3 + 3^3 + ... + n^3 = (n(n+1)/2)^2
#Example: n = 3 -> 1 + 8 + 27 = 36

n = int(input("Enter a positive integer n: "))
cube_sum = (n * (n + 1) // 2) ** 2
print(f"Sum of cubes from 1 to {n}: {cube_sum}")