class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        for (idx, num) in enumerate(numbers):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], idx + 1]
            lookup[num] = idx + 1
        return [-1, -1]