#Implement a function to find all subsets (power set) of a given set of distinct integers.
#Example: [1, 2, 3] -> [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Subsets: {subsets(nums)}")