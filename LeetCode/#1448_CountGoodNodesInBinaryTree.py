# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def helper(node, maximum):
            nonlocal cnt
            if node is None:
                return
            if node.val >= maximum:
                cnt += 1
            helper(node.left, max(maximum, node.val))
            helper(node.right, max(maximum, node.val))

        maximum = -1e10
        helper(root, maximum)
        return cnt


s = Solution()
print(s.goodNodes(TreeNode(3, TreeNode(1, TreeNode(3, None, None), None), TreeNode(4, TreeNode(1, None, None), TreeNode(5, None, None)))))
print(s.goodNodes(TreeNode(3, TreeNode(3, TreeNode(4, None, None), TreeNode(2, None, None)), None)))
print(s.goodNodes(TreeNode(1, None, None)))
