#Given a positive integer, check if it is an Armstrong number (sum of its own digits each raised to the power of the number of digits equals the number).
#Example: 153 = 1^3 + 5^3 + 3^3 = 153 -> True

num = int(input("Enter a positive integer: "))
order = len(str(num))
sum_pow = sum(int(d) ** order for d in str(num))
print(f"{num} is Armstrong: {sum_pow == num}")