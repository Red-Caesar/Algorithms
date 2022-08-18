nums = [1,2,3,4,5,6,7]
k = 3
arr = [_ for _ in nums]
for i in range(len(nums)):
    nums[(i+k)%len(nums)] = arr[i]
print(nums)