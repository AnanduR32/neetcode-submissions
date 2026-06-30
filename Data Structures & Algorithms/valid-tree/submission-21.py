class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMat = {x:set() for x in range(n)}
        visited = set()

        for (node_x, node_y) in edges:
            adjMat[node_x].add(node_y)
            adjMat[node_y].add(node_x)
        
        def checkForCycle(node:int, parent: int) -> Optional[bool]:
            if node in visited:
                return False
            visited.add(node)

            for next_node in adjMat[node]:
                if next_node in visited:
                    if next_node is parent:
                        continue
                    return False
                if checkForCycle(next_node, node) is False:
                    return False
        count = 0
        for node_x, _ in adjMat.items():
            if node_x not in visited:
                if checkForCycle(node_x, -1) is False:
                    return False
                count += 1

 

        return count == 1

    
                    