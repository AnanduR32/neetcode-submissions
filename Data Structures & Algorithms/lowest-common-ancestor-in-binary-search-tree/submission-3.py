# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if p.val > q.val:
            p,q = q, p
        # root is LCF
        if root.val >= p.val and root.val <= q.val:
            return root
        # LCF is to the left
        elif root.val >= p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p,q)
        # LCF is to the right
        elif root.val < p.val and root.val <= q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # LCF doesn't exist?
        else:
            return None