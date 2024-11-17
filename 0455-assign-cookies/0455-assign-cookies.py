class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        #size of s(cookise)
        m =len(s)
        #n is size of child list
        n = len(g)
        g.sort()
        s.sort()
        while(l<m and r<n):
            if g[r]<=s[l]:
                r+=1
            l+=1
        return r

                