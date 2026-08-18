from collections import deque
class MinStack:

    def __init__(self):
        self.minStack = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        self.minStack.appendleft(min(val,self.minStack[0] if self.minStack else val))

    def pop(self) -> None:
        self.stack.popleft()
        self.minStack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minStack[0]
        
