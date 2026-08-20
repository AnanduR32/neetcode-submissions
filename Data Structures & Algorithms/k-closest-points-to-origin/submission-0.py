class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        def distance(x,y):
            return math.sqrt(y**2 + x**2)
        [heapq.heappush(q, (distance(coord_x,coord_y), [coord_x,coord_y])) for coord_x,coord_y in points]

        output = []
        for _ in range(k):
            output.append(heapq.heappop(q)[1])

        return output