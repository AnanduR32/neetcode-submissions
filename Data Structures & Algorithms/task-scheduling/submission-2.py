from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        mapping = dict()
        heap = []
        cooldown = deque()
        
        for task in tasks:
            mapping[task] = mapping.get(task, 0) + 1

        for k, v in mapping.items():
            heapq.heappush(heap, -v)

        cycle = 0
        # heap has tasks frequencies in descending order
        while heap or cooldown:
            # take highest frequency in heap
            if heap:        
                count = -heapq.heappop(heap)
                # decrease frequency to denote task execution
                count -= 1
                # if task still pending then add to cooldown
                if count > 0:
                    cooldown.append((cycle + n, count))
            # check cooldown queue for all tasks which have cooled down
            while cooldown and cooldown[0][0] <= cycle:
                cooled_off = cooldown.popleft()[1]
                heapq.heappush(heap,-cooled_off)
            cycle += 1
            

        return cycle

        
