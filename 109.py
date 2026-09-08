#Implement bubble sort to sort a list of numbers in ascending order.
#Example: [5, 1, 4, 2, 3] -> [1, 2, 3, 4, 5]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print("Sorted:", nums)