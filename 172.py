#Implement a function to determine if a string is a palindrome permutation.
#A palindrome permutation is a rearrangement of the characters that can form a palindrome.
#Example: "code" -> False, "aab" -> True (can be "aba"), "carrace" -> True (can be "racecar")

def is_palindrome_permutation(s):
    s = s.replace(" ", "").lower()
    odd_count = 0
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1

text = input("Enter a string: ")
print(f"Is palindrome permutation: {is_palindrome_permutation(text)}")