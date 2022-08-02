nums = [-1,-1,0,0,-1,-1]
sum_n = [0 for _ in range(len(nums)+1)]
for i in range(1, len(sum_n)):
    sum_n[i] = sum_n[i-1] + nums[i-1]
print(sum_n)
ans = -1
for i in range(len(sum_n)-1):
    if sum_n[i] == sum_n[len(sum_n)-1] - sum_n[i] - nums[i]:
        ans = i
        break
print(ans)
