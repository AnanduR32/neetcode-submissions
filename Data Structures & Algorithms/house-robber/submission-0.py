class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        profit = [0 for _ in range(size+2)]
        best = 0
        for (idx, num) in enumerate(nums):
            profit_idx = idx + 2
            best = max((profit[profit_idx - 2] + num), profit[profit_idx - 1])
            profit[profit_idx] = best
        return best