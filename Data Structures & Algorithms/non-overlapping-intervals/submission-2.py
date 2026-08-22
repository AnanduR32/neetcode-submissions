class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = []
        
        intervals.sort()
        size = len(intervals)
        count = 0
        prevEnd = intervals[0][1]
        for idx in range(1,size):
            if intervals[idx][0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, intervals[idx][1])
            else:
                prevEnd = intervals[idx][1]
        
        return count