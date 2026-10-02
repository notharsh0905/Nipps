#Implement a function to remove duplicates from a list while preserving order.
#Example: [1, 2, 2, 3, 1, 4, 5] -> [1, 2, 3, 4, 5]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
seen = []
result = []
for num in nums:
    if num not in seen:
        seen.append(num)
        result.append(num)
print("Without duplicates:", result)