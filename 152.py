#Implement binary search on a rotated sorted array.
#Suppose an array is sorted in ascending order and then rotated at some pivot unknown to you.
#Example: [4, 5, 6, 7, 0, 1, 2], target=0 -> index 4

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Check which side is properly sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = list(map(int, input("Enter rotated sorted array (space-separated): ").split()))
target = int(input("Enter target: "))
print(f"Index: {search(nums, target)}")