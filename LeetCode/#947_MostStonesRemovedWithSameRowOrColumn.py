from typing import List

# didnt solve yet
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = sorted(stones, key=lambda x: (x[0],x[1]))
        cnt = 0
        i = 0
        while i < len(stones)-1:
            if stones[i][0] == stones[i+1][0]:
                del stones[i+1]
                cnt += 1
            else:
                i += 1
        i = 0
        while i < len(stones)-1:
            if stones[i][1] == stones[i+1][1]:
                del stones[i+1]
                cnt += 1
            else:
                i += 1

        return cnt


s = Solution()
print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(s.removeStones([[0,0]]))
