from tkinter.tix import Tree
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        def helper(node, nums, targetSum):
            nonlocal ans
            if node.left is None and node.right is None and targetSum - node.val == 0:
                ans.append(nums + [node.val])
        
            if node.left is not None:
                helper(node.left, nums + [node.val], targetSum - node.val)
            if node.right is not None:
                helper(node.right, nums + [node.val], targetSum - node.val)

        ans = []
        helper(root, [], targetSum)
    
        return ans 


s = Solution()
print(s.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22))
print(s.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
print(s.pathSum(TreeNode(1, TreeNode(2)), 0))
print(s.pathSum(None, 49))
