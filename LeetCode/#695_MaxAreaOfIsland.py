from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        queue = []
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1 or grid[i][j] == 0:
                    continue
                else:
                    queue.append((i, j))
                    s = 1
                    while queue:
                        n_i, n_j = queue.pop(0)
                        for x, y in step:
                            n_x = n_i + x
                            n_y = n_j + y
                            if 0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]) and grid[n_x][n_y] == 1:
                                queue.append((n_x, n_y))
                                s += 1
                                grid[n_i][n_j] = -1
                                grid[n_x][n_y] = -1
                    maximum = max(maximum, s)
        return maximum
