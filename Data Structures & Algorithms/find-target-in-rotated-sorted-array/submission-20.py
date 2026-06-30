class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[end]:  # [3,4,5,6,1,2]
                if nums[mid] > target >= nums[start]: # when target 5
                    end = mid
                else:                   # when target 2
                    start = mid + 1
            else:                       # [1,2,3,4,5,6]
                if nums[end] >= target > nums[mid]: # when target 5
                    start = mid + 1
                else:
                    end = mid        # when target 2
        return -1