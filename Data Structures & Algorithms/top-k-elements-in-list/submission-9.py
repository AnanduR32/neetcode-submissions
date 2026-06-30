import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for (num, freq) in count.items():
            heapq.heappush(heap,(freq, num))
            if (len(heap) > k):
                heapq.heappop(heap)
        return [x[1] for x in heap]
        