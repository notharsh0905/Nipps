#Calculate the sum of natural numbers from 1 to n using a while loop.
#Example: n = 10 -> 1 + 2 + 3 + ... + 10 = 55

n = int(input("Enter a positive integer n: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of first {n} natural numbers: {total}")