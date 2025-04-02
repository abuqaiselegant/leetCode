class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            else:
                profit = price-minPrice
                maxProfit =max(profit,maxProfit)
        return maxProfit