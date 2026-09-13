class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        start = 0 
        end = 1; 

        while end < len(prices):
            if (prices[start] < prices[end]):
                maxProfit = max(maxProfit, prices[end] - prices[start])
            else:
                start = end
            end += 1
        
        return maxProfit

