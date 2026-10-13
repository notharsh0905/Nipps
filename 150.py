#Implement a function to check if a string is an isogram (no repeating letters).
#Ignore case and spaces.
#Example: "Dermatoglyphics" -> True, "hello" -> False

def is_isogram(word):
    cleaned = word.lower().replace(" ", "")
    return len(cleaned) == len(set(cleaned))

text = input("Enter a word or phrase: ")
print(f"Is isogram: {is_isogram(text)}")