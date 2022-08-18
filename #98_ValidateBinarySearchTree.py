# 1st solution
# queq = [root]
# arr = [root.val]
# while queq:
#     link = queq.pop(0)
#     if link and link.left:
#         if link.left.val < link.val:
#             arr.insert(arr.index(link.val), link.left.val)
#             queq.append(link.left)
#         else:
#             return False
#     if link and link.right:
#         if link.right.val > link.val:
#             queq.append(link.right)
#             if arr.index(link.val) == len(arr) - 1:
#                 arr.append(link.right.val)
#             else:
#                 arr.insert(arr.index(link.val) + 1, link.right.val)
#         else:
#             return False
# return arr == sorted(arr) and len(arr) == len(set(arr))

# 2nd solution
import numpy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def rec(low, high, node):
        if not node: return True
        if low < node.val < high:
            return rec(low, node.val, node.left) and rec(node.val, high, node.right)
        else:
            return False

    return rec(-numpy.inf, +numpy.inf, root)