class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
            return False
        revHalf =0
        while x>revHalf:
            revHalf = revHalf*10+x%10
            x//=10
        if x==revHalf or x ==revHalf//10:
            return True
        else :
            return False
        """
        __________

        if x<0:
            return False
        if str(x)==str(x)[::-1] :
            return True
        else :
            return False
        ---------- 
        if x<0:
            return False

        rev = 0
        temp = x
        while temp>0:
            rem = temp%10
            rev = rev*10+rem
            temp=temp//10
        if rev == x:
            return True
        else :
            return False
        """

        
        