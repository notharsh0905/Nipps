#Implement a function to solve the 0/1 knapsack problem.
#Given weights and values of n items, determine the maximum value that can be put in a knapsack of capacity W.
#Example: weights = [1, 3, 4], values = [15, 20, 30], W = 4 -> max value 35 (items 1 and 3)

def knapsack(values, weights, W, n):
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return knapsack(values, weights, W, n - 1)
    else:
        return max(values[n - 1] + knapsack(values, weights, W - weights[n - 1], n - 1),
                   knapsack(values, weights, W, n - 1))

values = list(map(int, input("Enter values (space-separated): ").split()))
weights = list(map(int, input("Enter weights (space-separated): ").split()))
W = int(input("Enter knapsack capacity: "))
print(f"Maximum value: {knapsack(values, weights, W, len(values))}")