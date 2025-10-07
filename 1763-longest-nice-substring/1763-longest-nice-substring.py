class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        c = set(s)

        for i, ch in enumerate(s):
            if ch.islower():
                opposite = chr(ord(ch)-32)
            else:
                opposite = chr(ord(ch)+32)
            
            if opposite not in c:
                leftPart = self.longestNiceSubstring(s[:i])
                rightPart = self.longestNiceSubstring(s[i+1:])
                return leftPart if len(leftPart)>=len(rightPart) else rightPart
        return s
        