class TimeMap:

    def __init__(self):
        self.maxStamps = dict()
        self.stamps = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamps[key] = self.stamps.get(key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stamps:
            return ''
        low = 0
        high = len(self.stamps[key]) - 1
        possible_idx = -1
        if key in self.stamps:
            while low <= high:
                mid = (low + high) // 2
                if self.stamps[key][mid][0] == timestamp:
                    return self.stamps[key][mid][1]
                if self.stamps[key][mid][0] < timestamp:
                    possible_idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
        return self.stamps[key][possible_idx][1] if possible_idx >= 0 else ""

