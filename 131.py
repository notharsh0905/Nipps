#Implement a function to find the factorial of a number using tail recursion.
#Tail recursion is when the recursive call is the last operation in the function.

def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"{num}! = {factorial_tail(num)}")