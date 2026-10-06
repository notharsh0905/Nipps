#Implement a function to count the number of vowels in a given sentence.
#Consider both uppercase and lowercase vowels: a, e, i, o, u
#Example: "Hello World" -> 3 (e, o, o)

sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = sum(1 for ch in sentence if ch in vowels)
print(f"Number of vowels: {count}")