class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
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
        