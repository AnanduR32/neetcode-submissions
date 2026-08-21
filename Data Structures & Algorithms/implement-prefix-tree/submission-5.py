class PrefixTree:

    def __init__(self):
        self.tree = [None] * 26
        self.isValid = False

    def insert(self, word: str, idx = 0) -> None:
        size = len(word)
        if idx == size:
            self.isValid = True
            return 
        pos = ord(word[idx]) - 97
        if not self.tree[pos]:
            self.tree[pos] = PrefixTree()
        self.tree[pos].insert(word, idx + 1)

    def search(self, word: str, idx = 0) -> bool:
        size = len(word)
        if idx == size:
            return self.isValid

        pos = ord(word[idx]) - 97
        if self.tree[pos]:
            return self.tree[pos].search(word, idx + 1)
        return False

    def startsWith(self, prefix: str, idx = 0) -> bool:
        size = len(prefix)
        if idx == size:
            return True
        pos = ord(prefix[idx]) - 97
        if self.tree[pos]:
            return self.tree[pos].startsWith(prefix, idx + 1)
        return False
        
        