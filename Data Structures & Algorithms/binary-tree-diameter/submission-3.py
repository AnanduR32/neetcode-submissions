# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def findLength(root:TreeNode, count = 0)->int:
            nonlocal maxLength
            if root is None:
                return 0
            leftDepth = findLength(root.left, count + 1)
            rightDepth = findLength(root.right, count + 1)
            maxOfEither = max(leftDepth, rightDepth)
            maxLength = max(leftDepth + rightDepth, count + maxOfEither, maxLength)

            return 1 + maxOfEither
        
        findLength(root)

        return maxLength