from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(arr):
            nonlocal ans
            if len(arr) == len(nums):
                ans.append(arr)
                return
            for i in range(len(nums)):
                if nums[i] not in arr:
                    helper(arr + [nums[i]])

        helper([])
        return ans


s = Solution()
print(s.permute([1,2,3]))
print(s.permute([0,1]))
print(s.permute([1]))
