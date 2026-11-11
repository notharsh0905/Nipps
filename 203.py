#Implement the Two Sum problem.
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
result = two_sum(nums, target)
print(f"Indices: {result}")