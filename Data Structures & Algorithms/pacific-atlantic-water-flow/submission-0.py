class Solution:
    visited:List[List[List[bool]]] = []
    n_row:int = 0
    n_col:int = 0
    grid:List[List[int]]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.n_row = len(heights)
        self.n_col = len(heights[0])
        self.grid = heights
        self.visited = [[[False, False] for _ in range(self.n_col)] for _ in range(self.n_row)]
        
        for i in range(self.n_row):
            self.findPeakFromPacific(i, 0)
        for j in range(self.n_col):
            self.findPeakFromPacific(0, j)
        for i in range(self.n_row - 1, -1, -1):
            self.findPeakFromAtlantic(i, self.n_col - 1)
        for j in range(self.n_col - 1, -1, -1):
            self.findPeakFromAtlantic(self.n_row - 1, j)
        
        return [[i,j] for (i,row) in enumerate(self.visited) for (j,cell) in enumerate(row) if cell[0] == True and cell[1] == True]
    
    def findPeakFromPacific(self, i:int = 0, j:int = 0, prev: float = float('-inf')) -> None:
        if self.visited[i][j][0]:
            return
        if self.grid[i][j] >= prev:
            self.visited[i][j][0] = True
        else:
            return
        prev = self.grid[i][j]
        if i + 1 < self.n_row:
            self.findPeakFromPacific(i+1, j, prev)
        if j + 1 < self.n_col:
            self.findPeakFromPacific(i, j+1, prev)
        if i - 1 >= 0:
            self.findPeakFromPacific(i-1, j, prev)
        if j - 1 >= 0:
            self.findPeakFromPacific(i, j-1, prev)

    def findPeakFromAtlantic(self, i:int = 0, j:int = 0, prev: float = float('-inf')) -> None:
        if self.visited[i][j][1]:
            return
        if self.grid[i][j] >= prev:
            self.visited[i][j][1] = True
        else:
            return
        prev = self.grid[i][j]
        if i + 1 < self.n_row:
            self.findPeakFromAtlantic(i+1, j, prev)
        if j + 1 < self.n_col:
            self.findPeakFromAtlantic(i, j+1, prev)
        if i - 1 >= 0:
            self.findPeakFromAtlantic(i-1, j, prev)
        if j - 1 >= 0:
            self.findPeakFromAtlantic(i, j-1, prev)
    