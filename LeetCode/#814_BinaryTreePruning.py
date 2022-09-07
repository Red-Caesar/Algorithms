from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.right is None and root.left is None and root.val == 0:
            return None

        def helper(node):
            if node.left is not None:
                if helper(node.left):
                    node.left = None
            if node.right is not None:
                if helper(node.right):
                    node.right = None
            if node.left is None and node.right is None:
                return node.val == 0
        helper(root)
        return root


s = Solution()
print(s.pruneTree(TreeNode(1)))
print(s.pruneTree(TreeNode(0)))