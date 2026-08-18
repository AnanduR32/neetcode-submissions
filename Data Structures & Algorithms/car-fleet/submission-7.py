class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_tagged:list[tuple] = list()
        for idx, pos in enumerate(position):
            position_tagged.append((pos,idx))
        
        position_tagged.sort(key=lambda x: -x[0])
        times:list[int] = []

        for pos, speed_idx in position_tagged:
            times.append((target - pos) / speed[speed_idx])

        count = 1
        maxVal = times[0]
        for idx in range(1, len(times)):
            if times[idx] <= maxVal:
                continue
            maxVal = max(maxVal, times[idx])
            count += 1

        return count