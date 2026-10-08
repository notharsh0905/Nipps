#Implement a function to find the most frequent element in a list.
#If there are multiple elements with the same frequency, return the first one encountered.
#Example: [1, 3, 3, 3, 2, 2, 2] -> 3 (both 3 and 2 appear 3 times, but 3 appears first)

from collections import Counter

nums = list(map(int, input("Enter numbers separated by space: ").split()))
if nums:
    counter = Counter(nums)
    most_frequent = counter.most_common(1)[0][0]
    print(f"Most frequent element: {most_frequent}")
else:
    print("List is empty")