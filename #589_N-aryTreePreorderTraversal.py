
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 1st solution
# if not root: return []
#
# def rec(node, arr):
#     arr.append(node.val)
#     if not node.children:
#         return
#     for ch in node.children:
#         rec(ch, arr)
#
#
# arr = []
# rec(root, arr)
# return arr

# 2nd solution
if not root: return []
arr = []
children_q = []
arr_rev = []
children_q.append(root)
while children_q:
    node = children_q.pop(0)
    arr.append(node.val)
    for ch in node.children:
        arr_rev.append(ch)
    children_q = arr_rev + children_q
    arr_rev.clear()
return arr
