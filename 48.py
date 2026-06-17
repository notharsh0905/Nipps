# Take input from the user
user_input = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
lower_input = user_input.lower()

# Count vowels using sum and generator expression
vowel_count = sum(1 for char in lower_input if char in 'aeiou')

# Display the result
print(f"The number of vowels is: {vowel_count}")   