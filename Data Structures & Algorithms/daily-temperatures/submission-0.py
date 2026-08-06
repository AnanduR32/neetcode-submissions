from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = deque()
        out = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[0][0] < temp:
                pos = stack.popleft()[1]
                out[pos] = idx - pos
            stack.appendleft((temp,idx))

        return out
