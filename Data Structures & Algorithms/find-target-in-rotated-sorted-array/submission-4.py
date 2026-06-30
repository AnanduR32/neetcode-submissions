class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (right + left) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] >= nums[right]): # [3,4,5,6,7,8,1,2]
                if (nums[left] <= target < nums[mid]):
                    # go LHS
                    right = mid - 1
                else: 
                    # go RHS
                    left = mid + 1
            else:                           # [7,8,1,2,3,4,5,6]
                if (nums[mid] < target <= nums[right]):
                    # go RHS
                    left = mid + 1
                else:
                    # go LHS
                    right = mid - 1
        return -1
