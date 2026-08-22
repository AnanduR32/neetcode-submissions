class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = res = nums[0]
        size = len(nums)
        for idx in range(1,size):
            max_val = max(nums[idx], nums[idx] + max_val)

            res = max(max_val, res)

        return res