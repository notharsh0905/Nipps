#Print the Fibonacci sequence up to n terms.
#First two terms are 0 and 1, and each subsequent term is the sum of the previous two.
#Example: n = 7 -> 0, 1, 1, 2, 3, 5, 8

n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()