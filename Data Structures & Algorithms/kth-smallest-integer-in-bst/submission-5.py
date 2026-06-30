# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.goInorder(root, k)

    def goInorder(self, root: TreeNode, k: int) -> int:
        if root:
            if root.left:
                result = self.goInorder(root.left, k)
                if result != -1:
                    return result
            self.count += 1
            if self.count == k:
                return root.val
            if root.right:
                result = self.goInorder(root.right, k)
                if result != -1:
                    return result
        
        return -1