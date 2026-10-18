#Implement a function to find the nth Fibonacci number using dynamic programming with memoization.
#Store computed values in a cache to avoid redundant calculations.
#Example: F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, F(10) = 55

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

num = int(input("Enter n: "))
print(f"F({num}) = {fibonacci_memo(num)}")