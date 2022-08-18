m = 3
n = 7

#recursion
# def rec(x, y, cnt):
#     if x == n and y == m:
#         cnt[0] += 1
#         return
#     elif x > n or y > m:
#         return
#     rec(x + 1, y, cnt)
#     rec(x, y + 1, cnt)
#
#
# cnt = [0]
# rec(1, 1, cnt)
# print (cnt[0])

#dynamic programming
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
cnt = 0
dp[1][1] = 1
for x in range(1, n+1):
    for y in range(1, m+1):
        dp[y][x] += (dp[y-1][x] + dp[y][x-1])
print(dp[m][n])
