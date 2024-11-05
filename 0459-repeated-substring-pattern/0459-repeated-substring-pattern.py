class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i = 0
        letter = ""
        for i in range(l/2):
            letter = s[0:i+1]
            lL = len(letter)
            x= l//lL
            if letter*x==s:
                return True
        return False

        