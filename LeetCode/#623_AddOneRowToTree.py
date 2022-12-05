from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        if depth == 1:
            root = TreeNode(val, root, None) 
        while queue:
            
            if depth == 1:
                return root
            else:
                depth -= 1

            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                if depth == 1:
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                queue.append(node.left)
                queue.append(node.right)
            