class PrefixTree:

    def __init__(self):
        self.arr = [None] * 26
        self.endIn = False

    def insert(self, word: str) -> None:
        if not word:
            self.endIn = True
            return
        idx = ord(word[0].lower()) - 97
        if not self.arr[idx]:
            self.arr[idx] = PrefixTree() 
        self.arr[idx].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.endIn
        idx = ord(word[0].lower()) - 97
        if self.arr[idx]:
            return self.arr[idx].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        idx = ord(prefix[0].lower()) - 97
        if self.arr[idx]:
            return self.arr[idx].startsWith(prefix[1:])
        return False
        