class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row:list[set[int]] = [set() for _ in range(9)]
        col:list[set[int]] = [set() for _ in range(9)]
        box:list[set[int]] = [set() for _ in range(9)]
        def getBoxNum(i:int, j:int)->int:
            if i < 3:
                if j < 3:
                    return 0
                elif j < 6:
                    return 1
                else:
                    return 2
            elif i < 6:
                if j < 3:
                    return 3
                elif j < 6:
                    return 4
                else:
                    return 5
            else:
                if j < 3:
                    return 6
                elif j < 6:
                    return 7
                else:
                    return 8

        for i in range(0, 9):
            for j in range(0, 9):
                if not board[i][j].isdigit():
                    continue
                val = int(board[i][j])
                if val in row[i]:
                    return False

                if val in col[j]:
                    return False

                num = getBoxNum(i,j)
                if val in box[num]:
                    return False

                row[i].add(val)
                col[j].add(val)
                box[num].add(val)
                


        return True