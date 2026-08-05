class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row:list[set[str]] = [set() for _ in range(9)]
        col:list[set[str]] = [set() for _ in range(9)]
        box:list[set[str]] = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                val = board[i][j]
                if val in row[i]:
                    return False

                if val in col[j]:
                    return False

                num = (i // 3) * 3 + (j // 3)
                if val in box[num]:
                    return False

                row[i].add(val)
                col[j].add(val)
                box[num].add(val)
                


        return True