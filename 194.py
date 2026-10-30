#Implement a function to find the maximum subarray sum (Kadane's algorithm).
#Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum.
#Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6 (subarray [4, -1, 2, 1])

def max_subarray_sum(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Maximum subarray sum: {max_subarray_sum(nums)}")