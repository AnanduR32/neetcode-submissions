class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0: 0
        # 1: 1
        # 2: 1
        # 3: 2
        # 4: 1
        # 5: 2
        # 6: 2
        # 7: 3
        # 8: 1
        # 9: 2
        dp = [0] * (n + 1)
        for pos in range(1,n+1):
            dp[pos] = dp[pos >> 1] + (pos & 1)

        return dp


