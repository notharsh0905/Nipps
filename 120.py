#Implement quick sort to sort a list of numbers in ascending order.
#Using divide and conquer approach with pivot element.
#Example: [30, 10, 20, 5, 15] -> [5, 10, 15, 20, 30]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sorted:", quick_sort(nums))