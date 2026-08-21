class WordDictionary:

    def __init__(self):
        self.tree = [None] * 26
        self.isValid = False

    def addWord(self, word: str, idx = 0) -> None:
        size = len(word)
        
        if size == idx:
            self.isValid = True
            return

        pos = ord(word[idx]) - 97
        if not self.tree[pos]:
            self.tree[pos] = WordDictionary()
        self.tree[pos].addWord(word, idx + 1)

    def search(self, word: str, idx = 0) -> bool:
        size = len(word)
        
        if size == idx:
            return self.isValid

        if word[idx] == '.':
            for node in self.tree:
                if node and node.search(word, idx + 1):
                    return True
            return False
        else:
            pos = ord(word[idx]) - 97
            if self.tree[pos]:
                return self.tree[pos].search(word, idx + 1) 
            else:
                return False



