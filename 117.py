#Implement selection sort to sort a list of numbers in ascending order.
#Repeatedly find the minimum element from unsorted part and put it at the beginning.
#Example: [64, 25, 12, 22, 11] -> [11, 12, 22, 25, 64]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(nums)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if nums[j] < nums[min_idx]:
            min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
print("Sorted:", nums)