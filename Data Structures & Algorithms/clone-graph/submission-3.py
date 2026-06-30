"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque as Queue

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q:Queue = Queue()
        q.appendleft(node)
        visited = [False for _ in range(1,1001)]
        visited[node.val] = True
        clones:dict[Node] = dict()
        while q:
            curr_node = q.pop()
            if curr_node in clones:
                clone = clones[curr_node]
            else:
                clone = Node(curr_node.val)
                clones[curr_node] = clone 
            for neighbour in curr_node.neighbors:
                if not visited[neighbour.val]:
                    q.appendleft(neighbour)
                    visited[neighbour.val] = True
                if neighbour in clones:
                    neighbour_clone = clones[neighbour]
                else:
                    neighbour_clone = Node(neighbour.val)
                    clones[neighbour] = neighbour_clone 
                clone.neighbors.append(neighbour_clone)
        return clones[node]
