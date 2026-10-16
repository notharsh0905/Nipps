#Implement a function to check if two strings are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters.
#No two characters may map to the same character, but a character may map to itself.
#Example: "egg", "add" -> True, "foo", "bar" -> False

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping_s_t = {}
    mapping_t_s = {}
    for cs, ct in zip(s, t):
        if cs in mapping_s_t:
            if mapping_s_t[cs] != ct:
                return False
        else:
            if ct in mapping_t_s:
                return False
            mapping_s_t[cs] = ct
            mapping_t_s[ct] = cs
    return True

s = input("Enter first string: ")
t = input("Enter second string: ")
print(f"Isomorphic: {is_isomorphic(s, t)}")