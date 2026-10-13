#Implement a function to calculate the nth triangular number.
#The nth triangular number is the sum of the natural numbers from 1 to n.
#Formula: T_n = n(n+1)/2
#Example: T_1 = 1, T_2 = 3, T_3 = 6, T_4 = 10, T_5 = 15

n = int(input("Enter a positive integer n: "))
triangular = n * (n + 1) // 2
print(f"Triangular number T_{n} = {triangular}")