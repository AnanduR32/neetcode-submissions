class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        size = len(nums)
        nums.sort()
        def helper(start = 0, curr = []):
            nonlocal output
            output.append(curr[:])

            for idx in range(start, size): # start = 1, idx = 0
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue
                curr.append(nums[idx])
                helper(idx + 1, curr)
                curr.pop()
        helper()

        return output