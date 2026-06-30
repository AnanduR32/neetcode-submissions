class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        output = []
        freq_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))
        for idx, (key, value) in enumerate(freq_dict.items()):
            if idx < k:
                output.append(key)
        
        return output
