class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 3, 4, -3, 5, 2, -1
        # dp 1 
        # 3  12 12 12 12  12
        # dp 2
        # 3 12 -36 -180 360
        res = max_val = min_val = nums[0]
        
        size = len(nums)

        for idx in range(1,size):
            (min_val, max_val) = (
                min(nums[idx], nums[idx] * min_val, nums[idx] * max_val),
                max(nums[idx], nums[idx] * min_val, nums[idx] * max_val)
            )
            res = max(max_val, res)

        return res