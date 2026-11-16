#Implement a function to find the edit distance (Levenshtein distance) between two strings.
#The edit distance is the minimum number of operations (insert, delete, replace) required to transform one string into the other.
#Example: "kitten" and "sitting" -> 3 (k->s, e->i, insert g at the end)

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                   dp[i][j - 1],      # insert
                                   dp[i - 1][j - 1])  # replace
    return dp[m][n]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(f"Edit distance: {edit_distance(s1, s2)}")