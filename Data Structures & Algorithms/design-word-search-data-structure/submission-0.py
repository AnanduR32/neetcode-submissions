class WordDictionary:

    def __init__(self):
        self.arr = [None] * 26
        self.endIn = False

    def addWord(self, word: str) -> None:
        if not word:
            self.endIn = True
            return
        idx = ord(word[0].lower()) - 97
        if not self.arr[idx]:
            self.arr[idx] = WordDictionary()
        self.arr[idx].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.endIn
        
        if word[0] == '.':
            for idx in range(26):
                if self.arr[idx]:
                    response = self.arr[idx].search(word[1:])
                    if response:
                        return True
        else:
            idx = ord(word[0].lower()) - 97
            if self.arr[idx]:
                return self.arr[idx].search(word[1:])
        
        return False
