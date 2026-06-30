class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        curr = 0
        size = len(intervals)
        output: List[List[int]] = []
        inserted = False
        while curr < size:
            interval = None
            toInsert = False
            if not inserted and (newInterval[0] <= intervals[curr][0] or newInterval[0] <= intervals[curr][1]):
                lower = min(newInterval[0], intervals[curr][0])
                while curr + 1 < size and newInterval[1] >= intervals[curr + 1][0]:
                    curr += 1
                curr = min(curr, size - 1)
                toInsert = intervals[curr][0] > newInterval[1]
                upper = newInterval[1] if toInsert else max(newInterval[1], intervals[curr][1])
                interval = [lower, upper]
                inserted = True
            output.append(interval if interval else intervals[curr])
            if toInsert:
                output.append(intervals[curr])
            curr += 1
        if not inserted:
            output.append(newInterval)
        return output
