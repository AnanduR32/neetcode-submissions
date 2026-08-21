class Solution:
    def rob(self, nums: List[int]) -> int:
        #       2, 9, 8, 3, 6
        # 0, 0, 0, 0, 0, 0, 0
        size = len(nums)
        profit = [0] * (size + 2)

        for idx in range(size):
            profit[idx+2] = max(nums[idx] + profit[idx], profit[idx+1])
        
        return profit[-1]

