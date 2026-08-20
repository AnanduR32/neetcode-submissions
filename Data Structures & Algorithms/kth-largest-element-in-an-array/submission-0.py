import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        [heapq.heappush(q,-x) for x in nums]

        for _ in range(k - 1):
            heapq.heappop(q)
        
        return -q[0]