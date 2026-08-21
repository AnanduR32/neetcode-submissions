class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = [[] for _ in range(n)]
        visited = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node:int, idx:int=0)->bool:
            nonlocal visited

            visited.add(node)

            for dep in graph[node]:
                if dep == idx:
                    continue
                if dep in visited:
                    return False
                if not dfs(dep, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n