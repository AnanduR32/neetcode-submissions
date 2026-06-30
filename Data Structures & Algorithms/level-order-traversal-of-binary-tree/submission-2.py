# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = Queue()
        q.appendleft(root)
        result = []
        level: int = 0
        while q:
            level_size = len(q)
            current_level = []
            for _ in range(level_size):
                node = q.pop()
                current_level.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            result.append(current_level)
            
        return result
                
            
            