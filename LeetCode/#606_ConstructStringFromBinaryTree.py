from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        s = str(root.val)
        if root.left is not None:
            s += '(' + self.tree2str(root.left) + ')'
        if root.right is not None:
            if root.left is None:
                s += '()'
            s += '(' + self.tree2str(root.right) + ')'

        return s

s = Solution()
print(s.tree2str(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))
print(s.tree2str(TreeNode(1, TreeNode(2, None, TreeNode(4)),TreeNode(3, None, TreeNode(2)))))
print(s.tree2str(TreeNode(5)))
