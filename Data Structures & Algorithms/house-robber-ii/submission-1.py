class Solution:
        def rob(self, nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            size = len(nums)
            profit1 = [0 for _ in range(size+2)]
            profit2 = [0 for _ in range(size+2)]
            best1, best2 = 0, 0
            for idx in range(1, size):
                profit_idx = idx + 2
                best1 = max((profit1[profit_idx - 2] + nums[idx]), profit1[profit_idx - 1])
                profit1[profit_idx] = best1
            for idx in range(size - 1):
                profit_idx = idx + 2
                best2 = max((profit2[profit_idx - 2] + nums[idx]), profit2[profit_idx - 1])
                profit2[profit_idx] = best2
            return max(best1, best2)