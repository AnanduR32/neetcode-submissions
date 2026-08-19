# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftDepth = self.checkDepth(root.left)
        rightDepth = self.checkDepth(root.right)
        if math.fabs(rightDepth - leftDepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def checkDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.checkDepth(root.left), self.checkDepth(root.right))
