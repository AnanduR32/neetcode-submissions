class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = 0
        while start < end: 
            mid = (start + end) // 2
            if nums[mid] > nums[end]:    # [3,4,5,6,1,2]
                start = mid + 1
            else:                        # [1,2,3,4,5,6] [6,1,2,3,4,5]
                end = mid
        return nums[start]
