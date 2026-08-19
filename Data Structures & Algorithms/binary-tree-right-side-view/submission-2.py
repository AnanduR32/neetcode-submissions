# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.appendleft(root)
        output = list()
        while q:
            len_q = len(q)
            for idx in range(len_q):
                node = q.pop()
                if idx == len_q - 1:
                    output.append(node.val)

                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
        
        return output