class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest: int = prices[0]
        profit: int = 0 
        for iterator in range(1, len(prices)):
            profit = max(profit, prices[iterator] - smallest)
            smallest = min(smallest, prices[iterator])
        return profit