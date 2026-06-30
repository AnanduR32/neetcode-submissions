class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjMat = {x:set() for x in range(n)}

        for node_x, node_y in edges:
            adjMat[node_x].add(node_y)
            adjMat[node_y].add(node_x)

        def visitAllNodes(node:int, parent:int) -> Optional[bool]:
            if node in visited:
                return
            visited.add(node)
            for next_node in adjMat[node]:
                if next_node in visited:
                    continue
                visitAllNodes(next_node, node)
        
        count = 0
        for node_x, _ in adjMat.items():
            if node_x not in visited:
                visitAllNodes(node_x, -1)
                count += 1
        
        return count