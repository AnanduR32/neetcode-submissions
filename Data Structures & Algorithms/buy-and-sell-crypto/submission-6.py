class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        lowestVal = float('inf')
        maxProfit = 0

        for idx, price in enumerate(prices):
            # Two scenarios: Buy or not buy, if bought then sell or not sell
            maxProfit = max(maxProfit, price - lowestVal)
            lowestVal = min(price, lowestVal)
        
        return maxProfit
