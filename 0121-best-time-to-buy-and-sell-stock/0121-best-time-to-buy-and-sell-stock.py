class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit =0
        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice = prices[i]
        #     else:
        #         profit = prices[i]-minPrice
        #         maxProfit = max(profit, maxProfit)
        # return maxProfit
            # profit = prices[i]-minPrice
            # if profit>maxProfit:
            #     maxProfit = profit
            maxProfit = max(maxProfit, prices[i]-minPrice)

        return maxProfit






        # minPrice = prices[0]
        # maxProfit = 0
        # for price in prices[1:]:
        #     if price < minPrice:
        #         minPrice = price
        #     else:
        #         profit = price-minPrice
        #         maxProfit =max(profit,maxProfit)
        # return maxProfit