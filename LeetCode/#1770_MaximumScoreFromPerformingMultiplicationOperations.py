from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        def helper(num, mult, score):
            if len(mult) == 1:
                return score + max(mult[0]*num[0], mult[0]*num[-1])
            
            sc1 = helper(num[1:], mult[1:], score + mult[0]*num[0])
            sc2 = helper(num[:-1], mult[1:], score + mult[0]*num[-1])

            return max(sc1, sc2)

        return helper(nums, multipliers, 0)
s = Solution()
print(s.maximumScore([1,2,3], [3,2,1]))
print(s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))
print(s.maximumScore([555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10],
[783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521]))
