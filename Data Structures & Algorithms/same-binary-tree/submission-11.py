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

    def getInorder(self, root: TreeNode, char:str = '#') -> str:
        string = ""
        if root:
            string += str(root.val)
        else:
            string += char
            return string
        string += self.getInorder(root.left, 'L')
        string += self.getInorder(root.right, 'R')

        return string
