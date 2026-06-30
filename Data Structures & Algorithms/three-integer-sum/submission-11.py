class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        output : List[List[int]] = []
        for (idx, curr) in enumerate(nums):
            left = idx + 1
            right = size - 1
            if idx > 0 and (curr == nums[idx - 1]):
                continue
            while right > left:
                total = nums[left] + curr + nums[right]
                if (total == 0):
                    output.append([curr, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while (right > left and right < size - 1 and nums[right + 1] == nums[right]):
                        right -= 1
                    while (left > 0 and left < right and nums[left - 1] == nums[left]):
                        left += 1
                elif (total > 0):
                    right -= 1
                else:
                    left += 1 
        return output 
        # -4 -1 -1 0 1 2