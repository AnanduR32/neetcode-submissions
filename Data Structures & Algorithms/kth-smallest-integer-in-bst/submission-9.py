# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans, count = -1, 0
        def inorder(node):
            nonlocal ans, count
            if node is None or ans != -1:
                return None

            inorder(node.left)
            count += 1

            if count == k:
                ans = node.val
                return None
            
            inorder(node.right)

        inorder(root)

        return ans
        