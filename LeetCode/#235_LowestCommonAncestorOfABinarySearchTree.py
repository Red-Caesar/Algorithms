# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right
root = TreeNode(6, TreeNode(2, TreeNode(0, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(5, None, None))), TreeNode(8, TreeNode(7, None, None), TreeNode(9, None, None)))
p = TreeNode(2, TreeNode(0, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(5, None, None)))
q = TreeNode(8, TreeNode(7, None, None), TreeNode(9, None, None))
path_p = [root]
path_q = [root]
p_link = root
q_link = root
while p_link or q_link:
    if p_link:
        if p_link.val > p.val:
            p_link = p_link.left
        elif p_link.val < p.val:
            p_link = p_link.right
        else:
            p_link = None
        path_p.insert(0, p_link)
    if q_link:
        if q_link.val > q.val:
            q_link = q_link.left
        elif q_link.val < q.val:
            q_link = q_link.right
        else:
            q_link = None
        path_q.insert(0, q_link)
for i in range(len(path_p)):
    if path_p[i] and path_p[i] in path_q:
        print(path_p[i])
