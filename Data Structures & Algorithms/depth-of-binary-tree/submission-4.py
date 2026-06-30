# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], count:int = 0) -> int:
        if root is None:
            return 0
        countLeft = 0
        countRight = 0
        if root.left:
            countLeft = self.maxDepth(root.left)
        if root.right:
            countRight = self.maxDepth(root.right)
            
        return 1 + max(countLeft, countRight)
