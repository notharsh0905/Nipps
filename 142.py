#Implement a function to remove all vowels from a given string.
#Return the modified string without vowels (a, e, i, o, u, both uppercase and lowercase).
#Example: "Hello World" -> "Hll Wrld"

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in s if ch not in vowels)

sentence = input("Enter a sentence: ")
print(f"Without vowels: {remove_vowels(sentence)}")