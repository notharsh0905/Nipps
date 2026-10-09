#Implement a function to check if a string has all unique characters.
#Return True if no character repeats, False otherwise.
#Assume the string contains only ASCII characters.
#Example: "abcde" -> True, "aabc" -> False

def has_unique_chars(s):
    return len(set(s)) == len(s)

sentence = input("Enter a string: ")
print(f"All unique characters: {has_unique_chars(sentence)}")