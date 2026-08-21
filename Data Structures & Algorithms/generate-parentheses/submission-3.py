from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = deque()
        def helper(word:str = '', left:int = 0, right:int = float('inf'), stack = deque())->None:
            nonlocal output
            if right == 0:
                output.append(word)
                return
            if left < n:
                stack.appendleft('(')
                helper(word + '(', left + 1, right, deque(stack))
                stack.popleft()
            if right > 0 and stack:
                stack.popleft()
                helper(word + ')', left, right - 1, stack)
        
        helper('',0,n, stack)

        return output