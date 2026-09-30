#Implement linear search to find a target value in a list of numbers.
#Return the index of the target if found, otherwise -1.
#Example: [10, 20, 30, 40, 50], target=30 -> index 2

nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

for i, num in enumerate(nums):
    if num == target:
        print(f"Found at index: {i}")
        break
else:
    print("Not found, return -1")