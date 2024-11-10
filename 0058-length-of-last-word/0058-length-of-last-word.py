class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        a = s.split()
        last = a[len(a)-1]
        return len(last)        