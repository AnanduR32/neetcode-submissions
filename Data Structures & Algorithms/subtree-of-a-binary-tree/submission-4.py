# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot or not root:
            return subRoot == root
        return self.isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, root:TreeNode,subRoot:TreeNode):
        if not subRoot or not root:
            return subRoot == root
        return (root.val == subRoot.val) and self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)