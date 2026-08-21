"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        d = {node:Node(node.val)}
        q = [node]

        while q:
            currNode = q.pop()
            for neighbor in currNode.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                d[currNode].neighbors.append(d[neighbor])
        
        return d[node]