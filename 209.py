#Given a sentence, reverse the order of its words.
#Example: "hello world python" -> "python world hello"

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print("Reversed words:", reversed_sentence)