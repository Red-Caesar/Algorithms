from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def rec(ans, nums, start):
            if len(nums) == k and len(set(nums)) == len(nums):
                ans.append(nums)
                return
            for i in range(start, n+1):
                rec(ans, nums + [i], i+1)

        ans = []
        rec(ans, [], 1)
        return ans


s = Solution
print(s.combine(s, 4, 2))
print(s.combine(s, 5, 3))
print(s.combine(s, 1, 1))