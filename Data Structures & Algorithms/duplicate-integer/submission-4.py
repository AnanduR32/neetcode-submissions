class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        samples:set[int] = set()
        for num in nums:
            if num in samples:
                return True
            samples.add(num)
        return False