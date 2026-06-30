class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        goal = size - 1
        for idx in range(size - 1, -1, -1):
            if nums[idx] + idx >= goal:
                goal = idx
        return goal == 0