class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a = set(nums)
        if len(set_a) != len(nums):
            return True
        else:
            return False