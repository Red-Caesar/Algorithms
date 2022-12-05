# Not finished
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0 or len(prices) == 1:
            return 0

        profit = 0
        mn = 1001
        ans = []
        for i in range(len(prices)):
            if mn > prices[i] or profit >= prices[i]:
                ans.append(profit)
                mn = prices[i]
                profit = 0
            profit = max(profit, prices[i] - mn)    
        ans.append(profit)
        ans.sort(reverse=True)
        summary = 0
        for i in range(len(ans)):
            if i < k:
                summary += ans[i]
            else:
                break    
        return summary


s = Solution()
print(s.maxProfit(2, [2,4,1]))
print(s.maxProfit(2, [3,2,6,5,0,3]))
print(s.maxProfit(2, [3,2,3,5,1,6]))
print(s.maxProfit(2, [3,2,1,2,9,10,15]))
print(s.maxProfit(0, [3,2,6,5,0,3]))
print(s.maxProfit(3, []))
print(s.maxProfit(1, [2]))
print(s.maxProfit(2, [5,5,5,5,5,5]))
print(s.maxProfit(2, [6,1,3,2,4,7]))
print(s.maxProfit(2, [2,1,2,1,0,1,2]))
