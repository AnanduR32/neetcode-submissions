# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStr = self.getInorder(p)
        qStr = self.getInorder(q)
        print(pStr,qStr)
        return pStr == qStr

    def getInorder(self, root: TreeNode) -> str:
        string = ""
        if root:
            string += str(root.val)
        else:
            string += '#'
            return string
        string += self.getInorder(root.left)
        string += self.getInorder(root.right)

        return string
