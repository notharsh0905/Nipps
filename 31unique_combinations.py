#Write a program to print all the unique combinations of 1,2,3 and 4
"""from itertools import permutations

nums = [1, 2, 3, 4]

for p in permutations(nums):
    print(*p)"""

nums = [1, 2, 3, 4]

for i in nums:
    for j in nums:
        for k in nums:
            for l in nums:
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    print(i, j, k, l)