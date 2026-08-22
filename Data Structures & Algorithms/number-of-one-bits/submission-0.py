class Solution:
    def hammingWeight(self, n: int) -> int:
        out:int = 0
        for i in range(0, 32):
            out += n & 1
            n >>= 1

        return out