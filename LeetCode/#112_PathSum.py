from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.right is None and root.left is None and (targetSum - root.val == 0):
            return True
        
        ans1, ans2 = False, False
        if root.left is not None:
            ans1 = self.hasPathSum(root.left, targetSum - root.val)
        if root.right is not None:
            ans2 = self.hasPathSum(root.right, targetSum - root.val)
        
        return (ans1 or ans2)