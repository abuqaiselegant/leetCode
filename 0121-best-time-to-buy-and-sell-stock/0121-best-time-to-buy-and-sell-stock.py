class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            profit = max(profit, prices[i]-minPrice )
        return profit









        # minPrice = prices[0]
        # maxProfit =0
        # for i in range(1,len(prices)):
        #     if prices[i]<minPrice:
        #         minPrice = prices[i]
        
        # #     else:
        # #         profit = prices[i]-minPrice
        # #         maxProfit = max(profit, maxProfit)
        # # return maxProfit

        #     profit = prices[i]-minPrice
        #     if profit>maxProfit:
        #         maxProfit = profit

        #     # maxProfit = max(maxProfit, prices[i]-minPrice)

        # return maxProfit

