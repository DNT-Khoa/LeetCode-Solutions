class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProfit = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
        
        return maxProfit