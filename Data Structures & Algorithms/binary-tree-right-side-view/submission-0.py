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
        
        level = 0

        q = deque()
        q.appendleft((level, root))
        mapping = dict()

        while q:
            l, node = q.pop()

            if l in mapping:
                mapping[l].append(node.val)
            else:
                mapping[l] = [node.val]

            if node.left:
                q.appendleft((l + 1, node.left))
            if node.right:
                q.appendleft((l + 1, node.right))
        
        return [y[-1] for key,y in mapping.items()]