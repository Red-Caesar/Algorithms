nums = [3,2,4]
target = 6
#1st solution
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])
#             break

#2nd solution
hash_map = dict()
for i in range(len(nums)):
    if nums[i] not in hash_map:
        hash_map[nums[i]] = [i]
    else:
        hash_map[nums[i]].append(i)
for i in range(len(nums)):
    if (target - nums[i]) in hash_map:
        if (i != hash_map[target - nums[i]][-1]):
            print([i, hash_map[target - nums[i]][-1]])
            break