triangle = [[-1],[-2,-3]]
sum_path = 0

dp = []
max_level = len(triangle) - 1
for row in triangle:
    for el in row:
        dp.append(el)


if max_level != 0:
    level = 0
    index = 0
    minimum = 0
    for i in range(1, len(dp)):
        if index == 0:
            if i == 1:
                level = 1
            index = 1
            dp[i] += dp[i - level]
            if level == max_level:
                minimum = dp[i]
        elif index == level:
            dp[i] += dp[i - level - 1]
            index = 0
            if level == max_level:
                minimum = min(minimum, dp[i])
            level += 1
        else:
            dp[i] += min(dp[i - level], dp[i - level - 1])
            index += 1
            if level == max_level:
                minimum = min(minimum, dp[i])
else:
    minimum = dp[0]
print(minimum)