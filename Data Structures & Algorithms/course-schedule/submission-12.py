class Solution:
    adjMatrix:dict = dict()
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjMatrix:dict = dict()
        for req in prerequisites:
            if req[0] == req[1]:
                return False
            if req[0] in self.adjMatrix and req[1] in self.adjMatrix[req[0]]:
                return False
            else:
                self.adjMatrix[req[1]] = self.adjMatrix.get(req[1], []) + [req[0]]
        for course in range(numCourses):
            if course in self.adjMatrix:
                return self.checkCycleByDfs(course, set())

        return True
    
    def checkCycleByDfs(self, course:int, visited:set) -> bool:
        if course in visited:
            return False
        visited.add(course)
        if course not in self.adjMatrix:
            return True
        for nextInLine in self.adjMatrix[course]:
            return self.checkCycleByDfs(nextInLine, visited)
        return True