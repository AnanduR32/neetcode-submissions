class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        space = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in space:
                return [space[complement], idx]
            else:
                space[num] = idx
        return [-1, -1]
