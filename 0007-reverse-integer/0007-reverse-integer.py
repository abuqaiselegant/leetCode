class Solution(object):
    def reverse(self, x):
        is_neg = x<0
        x = abs(x)

        reversed = 0
        while x>0 :
            digit = x%10
            if reversed > 214748364 or (reversed == 214748364 and digit > 7):
                return 0
            reversed = reversed*10 + digit
            x = x//10
        
        if is_neg:
            return -1*reversed
        else:
            return reversed

        
        
        