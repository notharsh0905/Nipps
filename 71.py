#Given a word, count the number of vowels (a, e, i, o, u) in it.
#Example: "education" -> e, u, a, i, o -> 5

word = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for ch in word if ch in vowels)
print("Number of vowels:", count)