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
        size = len(inorder)
        mapped_indices = {val:idx for idx,val in enumerate(inorder)}
        pre_idx = 0
        def helper(start_in, end_in)->TreeNode:
            nonlocal pre_idx, size
            if start_in > end_in:
                return None
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            in_idx = mapped_indices[root_val]
            

            root.left = helper(start_in, in_idx - 1)
            root.right = helper(in_idx + 1, end_in)

            return root
        return helper(0, size - 1)