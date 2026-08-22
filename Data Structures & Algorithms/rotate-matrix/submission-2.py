class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # (0,0) -> (0,2)
        # (0,1) -> (1,2)
        # (0,2) -> (2,2)

        for idx in range(n//2):
            matrix[idx], matrix[-(idx+1)] = matrix[-(idx+1)], matrix[idx]

        for i in range(n):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]


