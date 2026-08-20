class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        size = len(nums)
        def helper(start = 0, total = 0, curr = []):
            nonlocal output
            if total == target:
                output.append(curr[:])
            if total >= target:
                return
            
            for idx in range(start, size):
                curr.append(nums[idx])
                helper(idx, total+nums[idx], curr)
                curr.pop()
        helper()
        return output