# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val: int = -1001, max_val:int = 1001) -> bool:
        if root is None:
            return True
        if root.val > min_val and root.val < max_val:
            return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)
        return False