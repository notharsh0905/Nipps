#Implement a function to generate all permutations of a given list.
#Example: [1, 2, 3] -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def permute(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # backtrack
    backtrack(0)
    return result

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Permutations: {permute(nums)}")