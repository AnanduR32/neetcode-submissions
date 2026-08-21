class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        size = len(word)
        n_row = len(board)
        n_col = len(board[0])
        visited = [[False for _ in range(n_col)] for _ in range(n_row)]
        def helper(i:int, j:int, curr_idx: str, visited:list[list])->bool:
            # If search term is complete
            if curr_idx == size:
                return True

            # check boundary
            if (
                i >= n_row
                or i < 0
                or j >= n_col
                or j < 0
                or visited[i][j]
                or board[i][j] != word[curr_idx]
            ):
                return False

            visited[i][j] = True
            
            found = (
                helper(i, j + 1, curr_idx + 1, visited)
                or helper(i + 1, j, curr_idx + 1, visited)
                or helper(i, j - 1, curr_idx + 1, visited)
                or helper(i - 1, j, curr_idx + 1, visited)
            )

            visited[i][j] = False
            return found

        for i in range(n_row):
            for j in range(n_col):
                if helper(i,j,0,visited):
                    return True

        return False




