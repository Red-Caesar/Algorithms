from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0:
            return False
        hash_map = dict()
        start, end = 0, 0
        while end < len(nums):
            if abs(start - end) > k:
                del hash_map[nums[start]]
                start += 1
            if nums[end] not in hash_map:
                hash_map[nums[end]] = 1
            else:
                return True
            end += 1
        return False


s = Solution()
# print(s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
# print(s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))              
        