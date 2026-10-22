#Implement a function to check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
#Example: "A man, a plan, a canal: Panama" -> True, "race a car" -> False

def is_palindrome(s):
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]

text = input("Enter a string: ")
print(f"Is palindrome: {is_palindrome(text)}")