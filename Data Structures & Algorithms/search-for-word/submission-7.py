class Solution:
    board: List[List[str]] = []
    n_row: int = 0
    n_col: int = 0
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.n_row = len(board)
        self.n_col = len(board[0])
        for i in range(self.n_row):
            for j in range(self.n_col):
                response = self.helper(word, i,j)
                if response:
                    return True
        return False

    def helper(self, word:str, i:int = 0, j:int = 0, visited:set[str]=set()) -> bool:
        key = f'{i}{j}'
        if key in visited:
            return False
        
        if self.board[i][j] == word[0]:
            word = word[1:]
        else:
            return False
        if not word:
            return True
        
        visited.add(key)
        left, right, up, down = False, False, False, False
        if i - 1 >= 0:
            left = self.helper(word, i - 1, j, visited)
        if j - 1 >= 0 and not left:
            up = self.helper(word, i, j - 1, visited)
        if j + 1 < self.n_col and not up:
            right = self.helper(word, i, j + 1, visited)
        if i + 1 < self.n_row and not right:
            down = self.helper(word, i + 1, j, visited)
        visited.remove(key)
        return left or right or up or down
