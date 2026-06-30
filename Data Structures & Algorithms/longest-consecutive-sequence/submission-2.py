class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        setEnds = set()
        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                setEnds.add(num)
        maxCount = 0
        for num in setEnds:
            count = 1
            currNum = num + 1
            while currNum in numSet:
                currNum += 1
                count += 1
            maxCount = max(maxCount, count)
        return maxCount
