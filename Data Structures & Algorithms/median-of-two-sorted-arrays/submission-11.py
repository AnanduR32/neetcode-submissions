class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        median = len(nums) // 2
        isEven = len(nums) % 2 == 0
        value = 0
        if isEven:
            value = (nums[median] + nums[median - 1]) / 2
        else:
            value = nums[median]
        
        return value


        
            