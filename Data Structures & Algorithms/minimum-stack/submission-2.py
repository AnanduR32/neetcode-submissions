from collections import deque
import heapq
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if self.minStack:
            self.minStack.appendleft(min(self.minStack[0], val))
        else:
            self.minStack.appendleft(val)
        
    def pop(self) -> None:
        self.stack.popleft()
        self.minStack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minStack[0]
