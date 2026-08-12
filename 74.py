#Given a list of numbers, count how many are even and how many are odd.
#Example: [1, 2, 3, 4, 5] -> even=2, odd=3

nums = list(map(int, input("Enter numbers separated by space: ").split()))
even = sum(1 for n in nums if n % 2 == 0)
odd = len(nums) - even
print(f"Even: {even}, Odd: {odd}")