class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]

        def helper(i:int, j:int)->None:
            nonlocal visited

            if (
                i == nrow
                or i < 0
                or j == ncol
                or j < 0
                or grid[i][j] == '0'
            ):
                return
            
            if visited[i][j]:
                return
            visited[i][j] = True

            helper(i + 1, j)
            helper(i, j + 1)
            helper(i, j - 1)
            helper(i - 1, j)


        for i in range(nrow):
            for j in range(ncol):
                if not visited[i][j] and grid[i][j]=='1':
                    count += 1
                    helper(i,j)
        return count
