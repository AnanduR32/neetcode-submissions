class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)

        ptr1 = 0
        ptr2 = 0

        isEven = (size1 + size2) % 2 == 0
        count = 0
        median = (size1 + size2) // 2
        prev = 0
        curr = 0
        while count < median and ptr1 < size1 and ptr2 < size2:
            if nums1[ptr1] <= nums2[ptr2]:
                prev = nums1[ptr1]
                ptr1 += 1
            else:
                prev = nums2[ptr2]
                ptr2 += 1
            count += 1        
        
        while count < median and ptr1 < size1:
            prev = nums1[ptr1]
            ptr1 += 1
            count += 1
        
        while count < median and ptr2 < size2:
            prev = nums2[ptr2]
            ptr2 += 1
            count += 1

        if ptr1 < size1 and ptr2 < size2:
            curr = nums1[ptr1] if nums1[ptr1] < nums2[ptr2] else nums2[ptr2]
        elif ptr1 < size1:
            curr = nums1[ptr1]
        else:
            curr = nums2[ptr2]
        
        print(prev, curr)
        
        return (curr + prev) / 2 if isEven else curr

        
            