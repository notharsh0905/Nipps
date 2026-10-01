#Check if a string is a palindrome using a while loop (comparing characters from both ends).
#Example: "madam" -> True, "hello" -> False

s = input("Enter a string: ").lower().replace(" ", "")
left, right = 0, len(s) - 1
is_palindrome = True
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(f'"{s}" is palindrome: {is_palindrome}')