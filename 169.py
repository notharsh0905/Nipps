#Implement a function to check if a parentheses string is valid.
#A string is valid if:
#- Open brackets must be closed by the same type of brackets.
#- Open brackets must be closed in the correct order.
#- An empty string is considered valid.
#Example: "()" -> True, "()[]{}" -> True, "(]" -> False

def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[ch] != top_element:
                return False
        else:
            stack.append(ch)
    return not stack

parentheses = input("Enter a parentheses string: ")
print(f"Is valid: {is_valid_parentheses(parentheses)}")