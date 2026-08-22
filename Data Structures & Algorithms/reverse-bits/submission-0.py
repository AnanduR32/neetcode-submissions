class Solution:
    def reverseBits(self, n: int) -> int:
        out:int = 0
        for _ in range(32):
            out = out << 1 | n & 1
            n = n >> 1
        return out