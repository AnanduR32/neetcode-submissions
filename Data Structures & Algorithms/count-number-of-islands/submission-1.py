class Solution:
    visited : List[List[bool]]
    n_row: int = 0
    n_col: int = 0
    grid: List[List[str]]
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n_row = len(grid)
        self.n_col = len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
        count = 0
        for i in range(self.n_row):
            for j in range(self.n_col):
                if not self.visited[i][j] and grid[i][j] == '1':
                    count += 1
                    self.doBfs(i,j)
        return count


    def doBfs(self,i,j) -> None:
        if self.visited[i][j] or self.grid[i][j] == '0':
            return
        self.visited[i][j] = True
        if i + 1 < self.n_row:
            self.doBfs(i+1, j)
        if j + 1 < self.n_col:
            self.doBfs(i, j+1)
        if i - 1 >= 0:
            self.doBfs(i-1, j)
        if j - 1 >= 0:
            self.doBfs(i, j-1)
        