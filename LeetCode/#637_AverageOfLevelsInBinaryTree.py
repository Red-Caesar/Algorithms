from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            sum = 0
            cnt = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is not None:
                    sum += node.val
                    cnt += 1
                    queue.append(node.left)
                    queue.append(node.right)
            if cnt != 0 :
                ans.append(sum/cnt)

        return ans


s = Solution()
print(s.averageOfLevels(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))
print(s.averageOfLevels(TreeNode(3, TreeNode(9, TreeNode(15, None, None), TreeNode(7, None, None)), TreeNode(20, None, None))))
print(s.averageOfLevels(TreeNode(0, None, None)))
