#Implement a solution to the Climbing Stairs problem.
#You are climbing a staircase with n steps, and you can either climb 1 or 2 steps at a time.
#Return the number of distinct ways to climb to the top.
#Example: n = 2 -> 2 ways (1+1, 2), n = 3 -> 3 ways (1+1+1, 1+2, 2+1)

def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

num = int(input("Enter number of steps: "))
print(f"Number of ways: {climb_stairs(num)}")