from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0 for _ in nums] for _ in range(2)]
        for i in range(len(nums)):
            if i == 0:
                dp[0][0] = nums[0]
            else:
                dp[0][i] = nums[i] + dp[1][i-1]
                dp[1][i] = max(dp[0][i-1], dp[1][i-1])
        return max(dp[0][len(nums)-1], dp[1][len(nums)-1])


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
