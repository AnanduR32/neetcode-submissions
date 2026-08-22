class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        nrow = len(matrix)
        ncol = len(matrix[0])
        cols = set()
        rows = set()
        for row_id, row in enumerate(matrix):
            for col_id, col in enumerate(row):
                if col == 0:
                    cols.add(col_id)
                    rows.add(row_id)
        for i in range(nrow):
            for j in range(ncol):
                if i in rows or j in cols:
                    matrix[i][j] = 0
            
        