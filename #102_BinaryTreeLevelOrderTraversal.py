# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# if not root: return []
# arr = []
# ch_q = [(root, 1)]
# while ch_q:
#     node = ch_q[0][0]
#     id = ch_q[0][1]
#     ch_q.pop(0)
#     if len(arr) < id:
#         arr.append([])
#         arr[id - 1].append(node.val)
#     else:
#         arr[id - 1].append(node.val)
#     if node.left is not None:
#         ch_q.append((node.left, id + 1))
#     if node.right is not None:
#         ch_q.append((node.right, id + 1))
# return arr
