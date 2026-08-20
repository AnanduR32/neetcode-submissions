# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder [2,1,3,4]
        # Inorder [1,2,3,4]
        preIdx = 0
        mapping = {val:idx for idx,val in enumerate(inorder)}
        def helper(start, end):
            nonlocal preIdx

            if start > end:
                return None
            
            node = TreeNode(preorder[preIdx])
            mid = mapping[preorder[preIdx]]

            preIdx += 1

            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)
            return node

        return helper(0, len(preorder) - 1)