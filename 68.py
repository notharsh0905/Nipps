#Given a string, check if it is a palindrome (reads the same forwards and backwards).
#Example: "racecar" -> True, "hello" -> False

s = input("Enter a string: ").strip()
if s == s[::-1]:
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')