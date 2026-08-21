class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since first and last house in array are adjacent
        # robber either decides to rob first house and not last
        # or doesn't rob first and can rob last
        # hence 2 scenarios:
        #   - Start at 0 and end one less
        #   - Start at 1 and end normally
        #    2, 9, 8, 3, 6
        # 0, 0, 0, 0, 0, 0
        size = len(nums)
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums)
        profit_1 = [0] * (size + 1)
        profit_2 = [0] * (size + 2)

        for idx in range(0,size - 1):
            profit_1[idx + 2] = max(nums[idx]+profit_1[idx], profit_1[idx + 1])
        
        for idx in range(1, size):
            profit_2[idx + 2] = max(nums[idx]+profit_2[idx], profit_2[idx + 1])
        return max(profit_1[-1], profit_2[-1])
