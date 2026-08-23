#Given a string, count the number of characters (excluding spaces).
#Example: "hello world" -> 11

s = input("Enter a string: ")
count = len(s.replace(" ", ""))
print("Number of characters (no spaces):", count)