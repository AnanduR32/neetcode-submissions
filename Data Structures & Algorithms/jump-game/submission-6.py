class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        jumpedToEnd = [False for _ in range(size)]
        jumpedToEnd[-1] = True
        for idx in range(size - 2, -1, -1):
            if nums[idx] == 0:
                continue
            for jumps in range(idx, min(idx + nums[idx] + 1, size)):
                if jumpedToEnd[jumps]:
                    jumpedToEnd[idx] = True
                    break
        
        return jumpedToEnd[0]