class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums = sorted(nums)
        output : List[List[int]] = []
        visited = set()
        for (idx, curr) in enumerate(nums):
            left, right = idx + 1, size - 1
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            while left < right:
                total = curr + nums[left] + nums[right]
                if total == 0:
                    output.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left< right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total <= 0:
                    left += 1
                else:
                    right -= 1

        return output
        # -4 -1 -1 0 1 2