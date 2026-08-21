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
            if i >= n_row or i < 0 or j >= n_col or j < 0:
                return False

            # check if visited
            if visited[i][j]:
                return False
            visited[i][j] = True
            
            # print(board[i][j], word[curr_idx])
            if board[i][j] == word[curr_idx]:
                curr_idx += 1
            else:
                visited[i][j] = False
                return False
            
            response = helper(i, j + 1, curr_idx, visited) or helper(i + 1, j, curr_idx, visited) or helper(i, j - 1, curr_idx, visited) or helper(i - 1, j, curr_idx, visited)

            visited[i][j] = False
            return response

        for i in range(n_row):
            for j in range(n_col):
                print(visited)
                result = helper(i,j,0,visited)

                if result:
                    return True

        return False




