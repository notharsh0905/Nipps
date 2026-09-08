#Check if two strings are anagrams of each other (contain the same characters in different order).
#Example: "listen" and "silent" -> True, "hello" and "world" -> False

s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")
print("Are anagrams:", sorted(s1) == sorted(s2))