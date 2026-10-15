#Implement a function to merge two sorted arrays into one sorted array.
#Example: [1, 3, 5] + [2, 4, 6] -> [1, 2, 3, 4, 5, 6]

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

arr1 = list(map(int, input("Enter first sorted array (space-separated): ").split()))
arr2 = list(map(int, input("Enter second sorted array (space-separated): ").split()))
print(f"Merged: {merge_sorted_arrays(arr1, arr2)}")