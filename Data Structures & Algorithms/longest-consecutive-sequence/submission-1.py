class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hSet = set(nums)
        currLength = 0
        maxLength = 0
        for value in hSet:
            if value - 1 not in hSet:
                offset = 1
                currLength = 1
                while value + offset in hSet:
                    currLength += 1
                    offset += 1
                maxLength = max(maxLength, currLength)
        return maxLength