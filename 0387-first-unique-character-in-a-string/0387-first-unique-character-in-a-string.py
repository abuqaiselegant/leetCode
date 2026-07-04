class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        for i in s:
            a[i] = a.get(i,0)+1
        x=''
        # print(a)
        for i in a:
            if a[i]==1:
                x=i
                break
        # print(x)
        for b in range(len(s)):
            if s[b]==x:
                return b
        return -1