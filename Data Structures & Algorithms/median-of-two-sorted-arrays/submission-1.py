class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = ptr2 = 0
        size1 = len(nums1)
        size2 = len(nums2)
        midPoint = (size1 + size2) // 2
        isEven = (size1 + size2) % 2 == 0
        arr = []
        pos = -1
        while(pos < midPoint):
            if (ptr1 < size1 and ptr2 < size2):
                if (nums1[ptr1] <= nums2[ptr2]):
                    arr.append(nums1[ptr1])
                    ptr1 += 1
                    pos +=1
                elif (nums1[ptr1] > nums2[ptr2]):
                    arr.append(nums2[ptr2])
                    ptr2 += 1
                    pos += 1
            if (ptr1 >= size1):
                while (ptr2 < size2 and pos < midPoint):
                    arr.append(nums2[ptr2])
                    ptr2 += 1
                    pos += 1
            if (ptr2 >= size2):
                while (ptr1 < size1 and pos < midPoint):
                    arr.append(nums1[ptr1])
                    ptr1 += 1
                    pos +=1
        if isEven:
            return (arr[-1] + arr[-2]) / 2
        else:
            return arr[-1]
            
            
            
            