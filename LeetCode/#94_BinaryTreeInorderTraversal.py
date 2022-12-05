from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        ans += self.inorderTraversal(root.left)
        ans += [root.val]
        ans += self.inorderTraversal(root.right)

        return ans



s = Solution()
print(s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))
print(s.inorderTraversal(None))
print(s.inorderTraversal(TreeNode(1)))
