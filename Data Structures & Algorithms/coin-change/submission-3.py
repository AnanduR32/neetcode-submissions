class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        size = len(coins)
        memo = dict()
        def helper(runningSum = 0):
            if runningSum == amount:
                return 0
            elif runningSum > amount:
                return float('inf')
            elif runningSum in memo:
                return memo[runningSum]

            minCoins = float('inf')
            for idx in range(size - 1, -1, -1):
                minCoins = min(minCoins, helper(runningSum + coins[idx]) + 1)
            memo[runningSum] = minCoins
            return minCoins
        coinsUsed = helper()
        return coinsUsed if coinsUsed != float('inf') else -1
            

