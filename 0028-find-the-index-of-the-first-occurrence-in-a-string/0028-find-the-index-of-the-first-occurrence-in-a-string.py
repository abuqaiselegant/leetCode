class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        

        index = haystack.find(needle)
        return index 
        """

        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i
        return -1
        
        