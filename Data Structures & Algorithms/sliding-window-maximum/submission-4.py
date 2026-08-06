from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        
        if size < k:
            return []
        
        heap = []
        maxVal = float('-inf')

        for idx in range(k):
            heapq.heappush(heap, (-nums[idx], idx))

        out:list[int] = [-heap[0][0]]
        for idx in range(k, size):
            while heap and heap[0][1] <= (idx - k):
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[idx], idx))
            out.append(-heap[0][0])
        return out

        