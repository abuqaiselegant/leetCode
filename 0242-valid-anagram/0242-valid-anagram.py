class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """a = sorted(s)
        b = sorted(t)
        if a==b:
            return True
        else :
            return False"""

        if len(s) != len(t):
            return False
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        for c in t:
            char_count[ord(c) - ord('a')] -= 1
            if char_count[ord(c) - ord('a')] < 0:
                return False
        return True