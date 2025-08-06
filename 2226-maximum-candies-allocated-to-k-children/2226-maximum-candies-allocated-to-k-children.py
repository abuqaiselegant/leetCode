class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        minCan = 1
        maxCan = max(candies)
        result = 0
        while minCan<=maxCan:
            mid = (minCan+maxCan)//2
            x=0
            for i in candies:
                x+=i//mid
            if x >= k:
                result =mid
                minCan =mid+1
            elif x<k:
                maxCan = mid-1
        return  result