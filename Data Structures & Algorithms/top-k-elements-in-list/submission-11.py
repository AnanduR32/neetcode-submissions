import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data : dict = {}
        heap = []
        for num in nums:
            data[num] = data.get(num, 0) + 1
        for key, value in data.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return list(y for x,y in heap)
        



        
        