from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue: deque[str] = deque()
        visited: set[str] = set()
        maxLength = 0
        for char in s:
            if char in visited:
                while queue and (current_item:= queue.popleft()) != char:
                    visited.remove(current_item)
                visited.add(char)
                queue.append(char)
            else:
                print(visited, char, queue)
                visited.add(char)
                queue.append(char)
                maxLength = max(maxLength, len(queue))
        return maxLength