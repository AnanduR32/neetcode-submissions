from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(','}':'{',']':'['}
        stack = deque()

        for char in s:
            if char in parentheses:
                if not stack:
                    return False
                opening = stack.popleft()
                if opening != parentheses[char]:
                    return False
            else:
                stack.appendleft(char)
        if stack:
            return False
        return True

