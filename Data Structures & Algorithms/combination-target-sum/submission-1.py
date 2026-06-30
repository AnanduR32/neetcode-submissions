class Solution:
    result = []
    def combinationSum(self, nums: List[int], target: int, arr: List[int] = []) -> Optional[List[List[int]]]:
        if not arr:
            self.result = []
        output = []
        if target == 0:
            self.result.append(arr)
            return
        if target < 0:
            return None
        for (toIgnore, num) in enumerate(nums):
            self.combinationSum(nums[toIgnore:], target - num, arr + [num])
        return self.result