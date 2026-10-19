#Implement a function to compress a string using the counts of repeated characters.
#If the compressed string would not become smaller, return the original string.
#Example: "aabcccccaaa" -> "a2b1c5a3", "abcdef" -> "abcdef" (no compression benefit)

def compress_string(s):
    compressed = []
    count = 1
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    compressed_str = "".join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

sentence = input("Enter a string: ")
print(f"Compressed: '{compress_string(sentence)}'")