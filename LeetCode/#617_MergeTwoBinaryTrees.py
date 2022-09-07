from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        queue1 = [root1]
        queue2 = [root2]
        while queue1:
            ref1 = queue1.pop(0)
            ref2 = queue2.pop(0)
            if ref2 and ref1 is not None:
                ref2.val += ref1.val
                if ref2.right is None and ref1.right is not None:
                    ref2.right = TreeNode(0, None, None)
                if ref2.left is None and ref1.left is not None:
                    ref2.left = TreeNode(0, None, None)
            else:
                continue
            queue1.append(ref1.left)
            queue1.append(ref1.right)
            queue2.append(ref2.left)
            queue2.append(ref2.right)

        return root2



s = Solution()
print(s.mergeTrees(TreeNode(1, TreeNode(3, TreeNode(5, None, None), None), TreeNode(2, None, None)), TreeNode(2, TreeNode(1, None, TreeNode(4, None, None)), TreeNode(3, None, TreeNode(7, None, None)))))
print(s.mergeTrees(TreeNode(1, None, None), TreeNode(1, TreeNode(2, None, None), None)))
print(s.mergeTrees(None, TreeNode(1, TreeNode(2, None, None), None)))
print(s.mergeTrees(TreeNode(1, TreeNode(2, None, None), None), None))
