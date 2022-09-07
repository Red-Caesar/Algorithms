from typing import List
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[-1].append(node.val)
                if node.children is not None:
                    for child in node.children:
                        if child is not None:
                            queue.append(child)
        return ans


s = Solution()
print(s.levelOrder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4, [Node(7)])])))
print(s.levelOrder(None))
