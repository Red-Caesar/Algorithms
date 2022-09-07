from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return

        def helper(node, parent):
            if node is None:
                return
            if parent is None:
                helper(node.left, node.right)
                helper(node.right, None)
            else:
                helper(node.left, node.right)
                helper(node.right, parent.left)
                node.next = parent

        helper(root, None)
        return root


s = Solution()
print(s.connect(Node(1,
                     Node(2, Node(4, None, None), Node(5, None, None)),
                     Node(3, Node(6, None, None), Node(7, None, None))
                     )
                )
      )
print(s.connect(None))
