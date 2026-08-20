class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        size = len(nums)

        def helper(curr = [], length = 0, used = set()):
            nonlocal output
            if length == size:
                output.append(curr[:])

            for idx in range(0, size):
                if idx in used:
                    continue
                used.add(idx)
                curr.append(nums[idx])
                helper(curr, length + 1, used)
                curr.pop()
                used.remove(idx)
            
        helper()
        return output
            