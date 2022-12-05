from functools import reduce
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def helper(node, num):
            nonlocal cnt
            num[node.val - 1] += 1 
            if node.left is None and node.right is None:
                if sum([x%2 != 0 for x in num]) <= 1:
                    cnt += 1
                num[node.val - 1] -= 1 
                return
            if node.left is not None:
                helper(node.left, num)
            if node.right is not None:
                helper(node.right, num)
            num[node.val - 1] -= 1
        helper(root, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        return cnt


s = Solution()
print(s.pseudoPalindromicPaths(TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))))
print(s.pseudoPalindromicPaths(TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))))
print(s.pseudoPalindromicPaths(TreeNode(9)))
