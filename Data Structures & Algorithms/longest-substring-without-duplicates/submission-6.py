from collections import deque as queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet: set[str] = set()
        q: queue = queue()
        maxLength = 0
        for char in s:
            if char in charSet:
                while q and (currVal:= q.pop()) and currVal != char:
                    charSet.remove(currVal)
                    continue
            charSet.add(char)
            q.appendleft(char)
            maxLength = max(maxLength, len(q))
        return maxLength