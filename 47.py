text = "Hello World"

# Safe search using find()
print(text.find('W'))  # Output: 6

# Search that raises error if missing
try:
    print(text.index('z'))
except ValueError:
    print("Character not found")   