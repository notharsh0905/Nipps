#Given a list of integers, find the second largest number.
#Assume the list has at least 2 distinct elements.
#Example: [1, 5, 3, 7, 2] -> 5

nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = sorted(set(nums), reverse=True)
print("Second largest:", unique_nums[1])