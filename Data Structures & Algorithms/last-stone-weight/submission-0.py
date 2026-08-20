import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        [heapq.heappush(q,-x) for x in stones]

        while len(q) > 1:
            a = -heapq.heappop(q)
            b = -heapq.heappop(q)
            c = abs(a - b)
            if c > 0:
                heapq.heappush(q, -c)
        
        if q:
            return -q[0]
        
        return 0
