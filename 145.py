#Implement a function to calculate the nth Fibonacci number using matrix exponentiation.
#This method has O(log n) time complexity compared to O(n) for iterative approach.
#F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5

def matrix_mult(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def matrix_pow(M, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, M)
        M = matrix_mult(M, M)
        n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    F = matrix_pow([[1, 1], [1, 0]], n - 1)
    return F[0][0]

num = int(input("Enter n: "))
print(f"F({num}) = {fibonacci(num)}")