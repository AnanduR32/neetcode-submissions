
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = dict()

        for num in nums:
            data[num] = data.get(num, 0) + 1
        count = 0
        result = [k for k,v in sorted(data.items(), key = lambda x:x[1], reverse=True)]
        return result[:k]