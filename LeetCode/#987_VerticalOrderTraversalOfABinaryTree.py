from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_table = dict()
        queue = deque()
        queue.append(root)
        hash_table[root] = (0, 0)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                x, y = hash_table[node]
                if node.left is not None:
                    queue.append(node.left)
                    hash_table[node.left] = (x + 1, y - 1)
                if node.right is not None:
                    queue.append(node.right)
                    hash_table[node.right] = (x + 1, y + 1)
        hash_table = sorted(hash_table.items(), key=lambda item: (item[1][1], item[0].val))
        index = next(iter(hash_table))[1][1]
        if index < 0:
            index = -index
        else:
            index = 0
        ans = []
        for key, value in hash_table:
            if value[1] + index < len(ans):
                ans[value[1] + index].append(key.val)
            else:
                ans.append([key.val])


        return ans


s = Solution()
print(s.verticalTraversal(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
print(s.verticalTraversal(TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(6, None, None)), TreeNode(3, TreeNode(5, None, None), TreeNode(7, None, None)))))
print(s.verticalTraversal(TreeNode(1, None, None)))