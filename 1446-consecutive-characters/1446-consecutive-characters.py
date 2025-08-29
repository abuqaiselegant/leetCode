class Solution:
    def maxPower(self, s: str) -> int:
        l = 0
        maxlen = 0
        count = 1
        if len(s)==1:
            return 1
        for r in range(1, len(s)):
            if s[r]==s[r-1]:
                count+=1
            if s[r]!=s[r-1]:
                l=r
                count = 1
            maxlen = max(count,maxlen)
        return maxlen
