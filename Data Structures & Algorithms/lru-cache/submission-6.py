from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = deque()
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            idx = self.q.index(key)
            del self.q[idx]
            self.q.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:    
            if len(self.q) == self.cap:
                val = self.q.pop()
                del self.cache[val]
            self.cache[key] = value
            self.q.appendleft(key)
        else:
            idx = self.q.index(key)
            del self.q[idx]
            self.q.appendleft(key)
            self.cache[key] = value


