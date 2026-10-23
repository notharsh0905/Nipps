#Implement binary search on a sorted list of integers.
#Return the index of the target if found, otherwise -1.
#Example: [1, 3, 5, 7, 9], target=5 -> index 2

nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter target: "))

left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(f"Found at index: {mid}")
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found, return -1")