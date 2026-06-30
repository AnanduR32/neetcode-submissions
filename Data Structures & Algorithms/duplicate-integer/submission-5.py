class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        samples:set[int] = set(nums)
        if len(nums) != len(samples):
            return True
        return False