# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l,r = 1,n
        while l<=r:
            mid =l+(r-l)//2
            res = guess(mid)
            if res>0:
                l=mid+1
            elif res==0:
                return mid
            else:
                r= mid-1
            