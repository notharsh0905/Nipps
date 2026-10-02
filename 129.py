#Find the second smallest number in a list of integers.
#Assume the list has at least 2 distinct elements.
#Example: [1, 5, 3, 7, 2] -> 2

nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = sorted(set(nums))
print("Second smallest:", unique_nums[1])