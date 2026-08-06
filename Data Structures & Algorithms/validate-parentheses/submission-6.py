from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        mapping = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for char in s:
            if char not in mapping:
                stack.appendleft(char)
            else:
                if not stack:
                    return False
                temp = stack.popleft()
                if temp != mapping[char]:
                    return False
        
        if len(stack) == 0:
            return True
        return False
