# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        result = False
        if root.val == subRoot.val:
            result = self.checkIfSame(root, subRoot)
        return result or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkIfSame(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val == q.val:
            return self.checkIfSame(p.left, q.left) and self.checkIfSame(p.right, q.right)
        else:
            return False

    