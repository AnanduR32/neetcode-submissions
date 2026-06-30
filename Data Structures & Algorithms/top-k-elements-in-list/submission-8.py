import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        for num in nums:
            if (num in count):
                count[num] += 1
            else:
                count[num] = 1
        for (num, freq) in count.items():
            heapq.heappush(heap,(freq, num))
            if (len(heap) > k):
                heapq.heappop(heap)
        return [x[1] for x in heap]
        