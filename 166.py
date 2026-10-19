#Implement insertion sort to sort a list of numbers in ascending order.
#Build the final sorted array one item at a time.
#Example: [12, 11, 13, 5] -> [5, 11, 12, 13]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
print("Sorted array:", nums)