class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        dp = [False for _ in range(size)]
        dp[-1] = True

        for idx in range(size - 2, -1, -1):
            curr_range = min(nums[idx], size - idx - 1)
            if curr_range == 0:
                continue
            for curr_idx in range(idx, idx + curr_range + 1):
                if dp[curr_idx]:
                    dp[idx] = True
                    continue
        
        return dp[0]