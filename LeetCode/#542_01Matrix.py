from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        isVisited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    for x, y in steps:
                        n_i = i + x
                        n_j = j + y
                        if 0 <= n_i < len(mat) and 0 <= n_j < len(mat[0]) and mat[n_i][n_j] == 1:
                            if not isVisited[n_i][n_j]:
                                queue.append((n_i, n_j))
                                isVisited[n_i][n_j] = True
        while queue:
            i, j = queue.popleft()
            for x, y in steps:
                n_i = i + x
                n_j = j + y
                if 0 <= n_i < len(mat) and 0 <= n_j < len(mat[0]) and mat[n_i][n_j] == 1:
                    if not isVisited[n_i][n_j]:
                        queue.append((n_i, n_j))
                        mat[n_i][n_j] += mat[i][j]
                        isVisited[n_i][n_j] = True
        return mat



s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(s.updateMatrix([[0]]))
print(s.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]))
