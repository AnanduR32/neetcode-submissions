# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode()
        
        root.val = preorder[0]
        pos_in_i = inorder.index(preorder[0])
        length_of_inorder_subset = pos_in_i
        
        left_preorder = preorder[1:length_of_inorder_subset+1]
        left_inorder = inorder[:pos_in_i+1]

        root.left = self.buildTree(left_preorder, left_inorder)

        right_preorder = preorder[1+length_of_inorder_subset:]
        right_inorder = inorder[pos_in_i + 1:]

        root.right = self.buildTree(right_preorder, right_inorder)

        return root
