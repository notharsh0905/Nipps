#Implement a function to find the longest common subsequence (LCS) between two strings.
#The LCS is the longest sequence of characters that appear in the same order in both strings.
#Example: "ABCDGH" and "AEDFHR" -> "ADH" (length 3)

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Reconstruct LCS
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(result))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
lcs_result = lcs(s1, s2)
print(f"LCS: '{lcs_result}', Length: {len(lcs_result)}")