class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currPurchaseVal = float('inf')
        profit = 0
        for price in prices:
            if price < currPurchaseVal:
                currPurchaseVal = price
            else:
                profit = max(profit, price - currPurchaseVal)
        return profit