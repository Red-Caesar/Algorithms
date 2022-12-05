from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append((entrance[0],entrance[1]))
        step = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maze[entrance[0]][entrance[1]] = -1
        cnt = 0
        while queue:
            cnt += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i, j in step:
                    if 0 <= x+i < len(maze) and 0 <= y+j < len(maze[0]):
                        if maze[x+i][y+j] == '.' and (x+i == 0 or x+i == len(maze)-1 or y+j == 0 or y+j == len(maze[0])-1):
                            return cnt
                        elif maze[x+i][y+j] == '.':
                            queue.append((x+i, y+j))
                            maze[x+i][y+j] = -1
        return -1
                        


s = Solution()
print(s.nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print(s.nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
print(s.nearestExit(maze = [[".","+"]], entrance = [0,0]))
print(s.nearestExit(maze = [["."]], entrance = [0,0]))
