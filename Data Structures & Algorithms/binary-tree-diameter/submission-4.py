# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def findLength(root:TreeNode)->int:
            nonlocal maxLength
            if root is None:
                return 0
            leftDepth = findLength(root.left)
            rightDepth = findLength(root.right)
            maxLength = max(leftDepth + rightDepth, maxLength)

            return 1 + max(leftDepth, rightDepth)
        
        findLength(root)

        return maxLength