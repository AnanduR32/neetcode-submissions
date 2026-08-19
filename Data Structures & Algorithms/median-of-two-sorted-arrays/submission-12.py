class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        median = len(nums1) // 2
        isEven = len(nums1) % 2 == 0
        value = 0
        if isEven:
            value = (nums1[median] + nums1[median - 1]) / 2
        else:
            value = nums1[median]
        
        return value


        
            