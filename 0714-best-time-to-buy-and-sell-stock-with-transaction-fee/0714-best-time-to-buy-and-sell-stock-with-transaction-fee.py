class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        cash = 0  # Maximum profit if no stock is held
        hold = -prices[0]  # Maximum profit if a stock is held
        
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)  # Either sell the stock or do nothing
            hold = max(hold, cash - prices[i])  # Either hold the stock or do nothing
        
        return cash
