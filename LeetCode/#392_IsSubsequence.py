s = "abbc"
t = "ahbdc"

#1st solution
# dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
# cnt = 0
# for i in range(1, len(s)+1):
#     for j in range(1, len(t)+1):
#         if s[i-1] == t[j-1]:
#             if dp[i - 1][j] == dp[i][j - 1] == dp[i-1][j-1]:
#                 cnt += 1
#         dp[i][j] = cnt
# ans = True if dp[len(s)][len(t)] == len(s) else False
# print(ans)

#2nd solution
if s:
    id = 0
    for i in range(len(t)):
        if t[i] == s[id]:
            id += 1
        if id == len(s):
            print(True)
    print(False)
else:
    print(True)
