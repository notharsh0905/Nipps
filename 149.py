#Implement a function to find the longest common prefix among a list of strings.
#If there is no common prefix, return an empty string.
#Example: ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> ""

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest

words = input("Enter strings separated by comma: ").split(",")
# Remove whitespace from each word
words = [w.strip() for w in words]
print(f"Longest common prefix: '{longest_common_prefix(words)}'")