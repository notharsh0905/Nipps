#Implement a function to find the intersection of two sorted lists.
#Return a new list containing only the distinct elements present in both lists.
#Example: [1, 2, 2, 3, 4] ∩ [2, 2, 3, 5] -> [2, 3]

def intersection(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            if not result or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
            j += 1
    return result

list1 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
list2 = list(map(int, input("Enter second sorted list (space-separated): ").split()))
print(f"Intersection: {intersection(list1, list2)}")