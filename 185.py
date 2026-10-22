#Implement a function to remove duplicates from a sorted array in-place.
#The relative order of the elements should be kept the same.
#Return the new length of the array after duplicates are removed.
#Example: nums = [1, 1, 2] -> length 2, nums = [1, 2, ...]

def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
new_length = remove_duplicates(nums)
print(f"New length: {new_length}, Modified array: {nums[:new_length]}")