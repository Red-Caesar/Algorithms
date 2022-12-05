from typing import List
from collections import deque

# havent solved
class Solution:
    pass
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     if len(board) == 1 and len(board[0]) == 1:
    #         return board[0][0] == word
    #     queue = deque()
    #     letters = [c for c in word]
    #     steps = [(0,1),(0,-1),(1,0),(-1,0)]
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == letters[0]:
    #                 if len(letters) == 1: return True
    #                 queue.append((i, j))
    #                 k = 1
    #                 used = [(i, j)]
    #                 while queue:
    #                     x, y = queue.popleft()
    #                     for step in steps:
    #                         n_x, n_y = step
    #                         if 0 <= x+n_x < len(board) and 0 <= y+n_y < len(board[0]) \
    #                                                         and k < len(letters) \
    #                                                         and board[x+n_x][y+n_y] == letters[k] \
    #                                                         and (x+n_x, y+n_y) not in used:
    #                             if k == len(letters)-1:
    #                                 return True
    #                             queue.append((x+n_x, y+n_y))
    #                             used.append((x+n_x, y+n_y))
    #                             k += 1
                                    
                        
                    
    #     return False




s = Solution()
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(s.exist(board = [["a"]], word = "a"))
print(s.exist(board = [["C","A","A"],["A","A","A"],["B","C","D"]], word = "AAB"))
