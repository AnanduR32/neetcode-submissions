# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        level = 0

        q.appendleft((level, root))
        mapping = dict()
        while q:
            l,node = q.pop()

            if l in mapping:
                mapping[l].append(node.val)
            else:
                mapping[l] = [node.val]

            if node.left:
                q.appendleft((l+1, node.left))
            if node.right:
                q.appendleft((l+1, node.right))
        
        return list(mapping.values())