class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        graph = [[] for num in range(numCourses)]
        for sub,dep in prerequisites:
            graph[sub].append(dep)

        def dfs(node, visiting = set()):
            nonlocal visited
            if node in visiting:
                return False
            if node in visited:
                return True
            
            visiting.add(node)
            for dep in graph[node]:
                if not dfs(dep, visiting):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for sub in range(numCourses):
            if graph[sub]:
                if sub not in visited:
                    if not dfs(sub):
                        return False

        return True
