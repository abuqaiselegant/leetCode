class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while temp>0:
            rem = temp%10
            rev = rev*10+rem
            temp=temp//10
        
        if rev == x:
            return True
        else:
            return False
