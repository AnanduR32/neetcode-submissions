class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        def insertNew(interval):
            nonlocal output
            if output and output[-1][1] >= interval[0]:
                existing = output.pop()
                if existing[1] > interval[1]:
                    interval[1] = existing[1]
                if existing[0] < interval[0]:
                    interval[0] = existing[0]
            output.append(interval)
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            insertNew(interval)
        
        return output