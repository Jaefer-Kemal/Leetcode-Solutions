class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float("inf")
        for r in range(len(prices)):
            if buy > prices[r]:
                buy = prices[r]
            
            sell = prices[r]
            max_profit = max(sell - buy, max_profit)
        
        return max_profit

