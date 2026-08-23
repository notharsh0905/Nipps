#Given a list of numbers, find the largest number using a loop (no built-in max).
#Example: [3, 7, 2, 9, 1] -> 9

nums = list(map(int, input("Enter numbers separated by space: ").split()))
largest = nums[0]
for n in nums[1:]:
    if n > largest:
        largest = n
print("Largest number:", largest)