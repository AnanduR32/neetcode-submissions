from collections import deque as queue
class Solution:
    def isValid(self, s: str) -> bool:
        q: queue = queue()
        isValid = True
        brackets = {'}':'{', ']':'[', ')':'('}
        for char in s:
            if char not in brackets:
                q.appendleft(char)
            else:
                if q and q[0] == brackets[char]:
                    q.popleft()
                else:
                    return False
        return not q

        
