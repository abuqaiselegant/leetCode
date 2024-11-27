class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = sys.maxsize
        profit =0
        for i in range(len(prices)):
            if prices[i]<min:
                min = prices[i]
            if (prices[i]-min)> profit:
                profit = prices[i]-min
        return profit