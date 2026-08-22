"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : (x.start, x.end))
        q = []
        for interval in intervals:
            if q and q[0] <= interval.start:
                heapq.heappop(q)
            heapq.heappush(q, interval.end)

        return len(q)

        