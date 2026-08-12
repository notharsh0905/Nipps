#Given the first term, common difference, and number of terms of an arithmetic progression (AP),
#find the sum of the series.
#Example: a=2, d=3, n=4 -> 2+5+8+11 = 26

a = int(input("First term (a): "))
d = int(input("Common difference (d): "))
n = int(input("Number of terms (n): "))
s = n * (2 * a + (n - 1) * d) // 2
print("Sum of AP series:", s)