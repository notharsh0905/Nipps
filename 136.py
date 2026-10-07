#Implement a function to find the median of a list of numbers.
#If the list has an odd number of elements, return the middle one.
#If the list has an even number of elements, return the average of the two middle values.
#Example: [1, 3, 5] -> 3, [1, 2, 3, 4] -> 2.5

nums = list(map(float, input("Enter numbers separated by space: ").split()))
nums.sort()
n = len(nums)
if n % 2 == 1:
    print(f"Median: {nums[n // 2]}")
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    print(f"Median: {median}")