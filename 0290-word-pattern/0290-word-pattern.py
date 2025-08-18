class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        a = {}
        c = {}
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in a and a[pattern[i]]!=s[i]:
                return False
            if s[i] in c and c[s[i]]!=pattern[i]:
                return False
            a[pattern[i]]=s[i]
            c[s[i]]=pattern[i]
        return len(c)==len(a)


                