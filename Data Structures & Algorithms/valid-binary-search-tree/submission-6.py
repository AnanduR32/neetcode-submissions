# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],  maxes:List[int] = [float('-inf'), float('inf')]) -> bool:
        
        if not root:
            return True
        if root.val <= maxes[0] or root.val >= maxes[1]:
            return False
        
        return self.isValidBST(root.left, [maxes[0], root.val]) and self.isValidBST(root.right, [root.val, maxes[1]])
