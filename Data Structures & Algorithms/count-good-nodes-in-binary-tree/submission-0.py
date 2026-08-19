# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def countGood(root, maxVal = float('-inf')):
            nonlocal count

            if not root:
                return None

            if root.val >= maxVal:
                maxVal = root.val
                count += 1
            
            countGood(root.left, maxVal)
            countGood(root.right, maxVal)
        countGood(root)

        return count
            
