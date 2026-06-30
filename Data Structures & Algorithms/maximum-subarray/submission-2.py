class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf') for _ in range(len(nums)+1)]
        for idx, num in enumerate(nums):
            dp[idx + 1] = max(dp[idx] + num, num)
        
        return max(dp)


