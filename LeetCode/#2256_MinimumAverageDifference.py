from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        minimum = (-1, 1e6)
        for i, n in enumerate(nums):
            prefix += n
            dif = abs(int(prefix/(i+1)) - int((total - prefix)/(len(nums)-i-1 + (i + 1) // len(nums))))
            if dif < minimum[1]:
                minimum = (i, dif)
        return minimum[0]
            

s = Solution()
# print(s.minimumAverageDifference([2,5,3,9,5,3]))
# print(s.minimumAverageDifference([0]))
print(s.minimumAverageDifference([0,1,0,1,0,1]))
