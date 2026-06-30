# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = {}
        q = deque()
        q.appendleft(root)
        result = []
        while q:
            arr = []
            nodes = []
            while q and (curr:= q.pop()):
                arr.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
            for node in nodes:
                q.appendleft(node)
            if arr:
                result.append(arr)
        
        return result




        