class Solution(object):
    def isPalindrome(self,s):
        s= s.lower()
        cleaned = []
        for c in s:
            if c.isalnum():
                cleaned.append(c)
        cleaned = ''.join(cleaned)
        if cleaned == cleaned[::-1]:
            return True
        else :
            return False
        