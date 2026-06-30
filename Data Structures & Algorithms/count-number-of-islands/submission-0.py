class Solution:
    visited: List[List[bool]]
    grid: List[List[str]]
    n_row: int
    n_col: int
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n_row = len(grid)
        self.n_col = len(grid[0])
        self.visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
        self.grid = grid
        count = 0
        for row in range(self.n_row):
            for col in range(self.n_col):
                if not self.visited[row][col] and grid[row][col] == '1':
                    count += 1
                    self.doBfs(row,col)
        return count

    def doBfs(self, row:int, col: int) -> None:
        if row >= self.n_row or col >= self.n_col or row == -1 or col == -1:
            return None 
        if self.visited[row][col] or self.grid[row][col] == '0':
            return None
        self.visited[row][col] = True
        self.doBfs(row+1, col)
        self.doBfs(row, col+1)
        self.doBfs(row-1, col)
        self.doBfs(row, col-1)
