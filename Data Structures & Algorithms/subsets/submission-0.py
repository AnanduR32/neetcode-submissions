class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [] 
        size = len(nums)

        def helper(idx = 0, curr = []):
            nonlocal output
            if idx == size:
                output.append(curr)
                return
            helper(idx + 1, curr + [nums[idx]]) #[1,3]
            helper(idx + 1, curr)
        
        helper()

        return output

