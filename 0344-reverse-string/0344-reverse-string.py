class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r] =s[r],s[l]
            l+=1
            r-=1
        
        
        
        
        
        # """
        # Do not return anything, modify s in-place instead.
        # """
        # start = 0
        # end = len(s)-1
        # while(start<end):
        #     '''temp = s[start]
        #     s[start]=s[end]
        #     s[end]= temp'''
        #     s[start], s[end]=s[end],s[start]
        #     start+=1
        #     end-=1
        