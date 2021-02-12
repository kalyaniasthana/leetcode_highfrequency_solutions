"""
 - keep track of the minimum price till now
 - keep track of the maximum profit till now => current_price - min_price

"""



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force is O(n**2), how can we improve? 
        n=len(prices)
        max_profit = 0
        min_price = float('Inf')
        for i in range(n):
            current_price = prices[i]
            if current_price < min_price:
                min_price = current_price
            current_profit = current_price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit
        