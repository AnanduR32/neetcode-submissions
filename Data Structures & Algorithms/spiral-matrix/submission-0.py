class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1  2  3  4
        # 5  6  7  8
        # 9  10 11 12
        # 13 14 15 16

        # 1  2  3  4
        # 8  6  7  5
        # 12 10 11 9
        # 16 14 15 13
        nrow = len(matrix)
        ncol = len(matrix[0])

        right, left, bottom, top = ncol - 1, 0, nrow - 1, 0
        output = []
        while top <= bottom and left <= right:
            # go right
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1
            
            # go down
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            # go left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            
            # go up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1

                    
        return output