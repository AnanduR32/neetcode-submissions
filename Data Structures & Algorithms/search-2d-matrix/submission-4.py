class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])

        desired_row_idx = -1
        left = 0
        right = n_row - 1
        while left < right:
            mid = (left + right)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid][-1] < target:
                    left = mid + 1
                else:
                    left = mid
                    break
            else:
                right = mid - 1
        desired_row = left
        left = 0
        right = n_col - 1
        while left >= 0 and left <= right and right < n_col:
            mid = (left + right)//2
            print(mid)
            if matrix[desired_row][mid] == target:
                return True
            elif matrix[desired_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False