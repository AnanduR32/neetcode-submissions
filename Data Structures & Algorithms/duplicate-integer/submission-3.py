class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        space:set[int] = set()
        for num in nums:
            if num in space:
                return True
            space.add(num)

        return False