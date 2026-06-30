# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque as Queue

class Solution:
    class Node:
        def __init__(self, level: int, node: TreeNode):
            self.level = level
            self.node = node
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = Queue()
        q.appendleft(self.Node(0, root))
        result = []
        lookup = {}
        level: int = 0
        while q and (current_node_obj:= q.pop()):
            if current_node_obj.node.left:
                q.appendleft(self.Node(current_node_obj.level + 1, current_node_obj.node.left))
            if current_node_obj.node.right:
                q.appendleft(self.Node(current_node_obj.level + 1, current_node_obj.node.right))
            if current_node_obj.level in lookup:
                lookup[current_node_obj.level].append(current_node_obj.node.val)
            else:
                lookup[current_node_obj.level] = [current_node_obj.node.val]
        for (k, v) in sorted(lookup.items()):
            result.append(v)
        return result
                
            
            