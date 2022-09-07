from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        isVisited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        isFresh = 0
        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    for x, y in steps:
                        n_i = i + x
                        n_j = j + y
                        if 0 <= n_i < len(grid) and 0 <= n_j < len(grid[0]) and grid[n_i][n_j] == 1:
                            if not isVisited[n_i][n_j]:
                                queue.append((n_i, n_j))
                                grid[i][j] = 0
                                maximum = max(maximum, grid[n_i][n_j])
                                isVisited[n_i][n_j] = True
                                isFresh -= 1
                if grid[i][j] == 1:
                    isFresh += 1

        while queue:
            i, j = queue.popleft()
            for x, y in steps:
                n_i = i + x
                n_j = j + y
                if 0 <= n_i < len(grid) and 0 <= n_j < len(grid[0]) and grid[n_i][n_j] == 1:
                    if not isVisited[n_i][n_j]:
                        queue.append((n_i, n_j))
                        grid[n_i][n_j] += grid[i][j]
                        maximum = max(maximum, grid[n_i][n_j])
                        isVisited[n_i][n_j] = True
                        isFresh -= 1

        return maximum if isFresh == 0 else -1


s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))
print(s.orangesRotting([[1,2]]))
