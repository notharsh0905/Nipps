#Given a positive integer, check if it is a perfect number.
#A perfect number equals the sum of its proper divisors (excluding itself).
#Example: 6 = 1 + 2 + 3 -> True

num = int(input("Enter a positive integer: "))
if num <= 1:
    print(f"{num} is not perfect")
else:
    sum_div = sum(i for i in range(1, num) if num % i == 0)
    print(f"{num} is perfect: {sum_div == num}")