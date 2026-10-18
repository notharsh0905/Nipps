#Implement a function to reverse the words in a given sentence.
#Example: "hello world practice" -> "practice world hello"
#Note: individual words are not reversed, only their order.

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence

sentence = input("Enter a sentence: ")
print(f"Reversed words: {reverse_words(sentence)}")