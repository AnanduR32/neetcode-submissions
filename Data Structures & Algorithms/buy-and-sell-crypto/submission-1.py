class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest: int = 999
        profit: int = 0 
        for price in prices:
            profit = max(profit, price - smallest)
            smallest = min(smallest, price)
        return profit