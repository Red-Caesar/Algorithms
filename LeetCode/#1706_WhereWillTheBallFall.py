from typing import List
from collections import deque

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        path = deque()
        ans = [-1 for _ in range(len(grid[0]))]
        for i in range(len(grid[0])):
            path.append((0, i))
            while path:
                x, y = path.popleft()
                if x >= len(grid):
                    ans[i] = y
                else:
                    if grid[x][y] == 1 and y != len(grid[0]) - 1 and grid[x][y+1] != -1:
                        path.append((x+1, y+1)) 
                    elif grid[x][y] == -1 and y != 0 and grid[x][y-1] != 1:
                        path.append((x+1, y-1)) 
        return ans

s = Solution()
print(s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(s.findBall([[-1]]))
print(s.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
