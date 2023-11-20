class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        buy = 0
        sell = 1
        
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
                sell += 1
            else:
                maxProfit = max(maxProfit, profit)
                sell += 1
        
        return maxProfit
        