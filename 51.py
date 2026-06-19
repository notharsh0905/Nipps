original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(original_list))
print(unique_list)  # Output: [1, 2, 3, 4, 5]   