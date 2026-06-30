# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], minVal: float = float('-inf'), maxVal: float = float('inf')) -> bool:
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        
        return self.isValidBST(root.left, minVal, root.val) and self.isValidBST(root.right, root.val, maxVal)


        