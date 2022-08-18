nums = [0,1,0,3,12]
k = 0
i = 0
while i < len(nums):
    if nums[k] == 0:
        nums.pop(k)
        nums.append(0)
        k -= 1
    i += 1
    k += 1
print(nums)