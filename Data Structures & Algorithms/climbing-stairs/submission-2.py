class Solution:
    def climbStairs(self, n: int) -> int:
        # [0,1,2,3,5]
        if n < 3:
            return n
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for idx in range(3, n + 1):
            ways[idx] = ways[idx - 1] + ways[idx - 2]

        return ways[-1]