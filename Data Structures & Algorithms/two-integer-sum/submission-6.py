class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            if num in complements:
                return [complements[num], idx]
            else:
                complement = target - num
                complements[complement] = idx

        return [] 