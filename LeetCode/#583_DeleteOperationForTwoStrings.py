word1 = "leetcode"
word2 = "etco"
dp = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
for i, c1 in enumerate(word1):
    for j, c2 in enumerate(word2):
        if c1 == c2:
            dp[i+1][j+1] = dp[i][j] + 1
        elif c1 != c2:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(len(word2)+len(word1) - 2*dp[len(word1)][len(word2)])