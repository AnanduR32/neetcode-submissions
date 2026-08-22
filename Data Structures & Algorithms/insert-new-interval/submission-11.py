class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        size = len(intervals)
        inserted = False

        if not intervals:
            return [newInterval]

        def insertIntoNew(interval:list):
            nonlocal output
            if output and interval[0] <= output[-1][1]:
                existing = output.pop()

                if existing[0] < interval[0]:
                    interval[0] = existing[0]
                if existing[1] > interval[1]:
                    interval[1] = existing[1]
            
            output.append(interval)                     

        pos = 0
        while pos < size:
            existing = intervals[pos]
            if newInterval[0] < existing[0] and not inserted:
                insertIntoNew(newInterval)
                inserted = True
            else:
                insertIntoNew(existing)
                pos += 1
        if not inserted:
            insertIntoNew(newInterval)
        return output
