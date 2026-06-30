class Solution:
    adjMat:dict
    visitedNodes:set
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adjMat = dict()
        self.visitedNodes = set()
        for (node_x,node_y) in edges:
            if node_x > node_y and node_x not in self.visitedNodes:
                node_x, node_y = node_y, node_x
            if node_x not in self.adjMat:
                self.adjMat[node_x] = set()
            self.adjMat[node_x].add(node_y)
            self.visitedNodes.add(node_x)
            self.visitedNodes.add(node_y)
        self.visitedNodes = set()
        count = 0
        print(self.adjMat)
        for node_x in range(n):
            if node_x not in self.visitedNodes:
                response = self.checkForCycle(node_x, {node_x})
                if response is False:
                    return False
                count += 1
        
        return count == 1

    def checkForCycle(self, node_x:int, visited:set) -> Optional[bool]:
        self.visitedNodes.add(node_x)
        if node_x not in self.adjMat:
            return
        for next_node_x in self.adjMat[node_x]:
            if next_node_x in self.visitedNodes:
                return False
            visited.add(next_node_x)
            print(visited)
            response = self.checkForCycle(next_node_x, visited)
            if response is False:
                return False
            
            visited.remove(next_node_x)
        