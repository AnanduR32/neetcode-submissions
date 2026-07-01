class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        for row_id in range(size//2):
            matrix[row_id], matrix[size - row_id - 1] = matrix[size - row_id - 1], matrix[row_id]
        
        for i in range(size):
            for j in range(i + 1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        