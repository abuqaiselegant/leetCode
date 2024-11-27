class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int minPrice = Integer.MAX_VALUE;
        for(int i =0;i<prices.length;i++){
            minPrice = Math.min(prices[i],minPrice);
            max = Math.max(max, prices[i] - minPrice);
        }
    return max;
    }

    // public int maxProfit(int[] prices){
    //     int min = Integer.MAX_VALUE;
    //     int profit = 0;
    //     for(int i = 0;i<prices.length;i++){
    //         if(prices[i]<min){
    //             min = prices[i];
    //         }
    //         if(profit<prices[i]-min){
    //             profit = prices[i]-min;
    //         }
    //     }
    //     return profit;
    // }

    
}