class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        goal = size - 1
        dp = [False for _ in range(size)]
        for idx in range(size - 1, -1, -1):
            if nums[idx] + idx >= goal:
                goal = idx
                dp[idx] = True
        return dp[0]