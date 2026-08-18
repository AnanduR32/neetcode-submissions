import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        q:heapq = []
        output = [0] * size

        for idx,temp in enumerate(temperatures):
            while q and q[0][0] < temp:
                output[q[0][1]] = idx - q[0][1]
                heapq.heappop(q) 
            
            heapq.heappush(q, (temp, idx))
        return output
