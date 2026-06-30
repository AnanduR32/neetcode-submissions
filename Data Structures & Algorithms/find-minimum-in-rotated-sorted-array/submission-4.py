class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        while (True):
            mid = (upper + lower) // 2
            if (mid == upper == lower):
                return nums[mid]
            if (nums[mid] > nums[mid+1]):
                return nums[mid + 1]
            
            if (nums[mid] > nums[upper]):
                lower = mid
            else:
                upper = mid