class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = sorted(s)
        b = sorted(t)
        if a==b:
            return True
        else :
            return False