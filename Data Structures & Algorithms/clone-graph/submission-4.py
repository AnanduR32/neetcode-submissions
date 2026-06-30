"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque()
        q.appendleft(node)

        copies:dict = {}
        while q:
            curr = q.pop() # 2
            copy_head: Node
            if curr in copies:
                copy_head = copies[curr]
            else:
                copy_head = Node(curr.val)
                copies[curr] = copy_head # Node(1, [])

            for neighbor in curr.neighbors: # [1,3]
                copy:Node
                if neighbor in copies:
                    copy = copies[neighbor] # 
                else:
                    copy = Node(neighbor.val)
                    copies[neighbor] = copy # Node(3,[])
                    q.appendleft(neighbor)
                copy_head.neighbors.append(copy)
        return copies[node]